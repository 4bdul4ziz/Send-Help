package main, idea

type Idea struct {
	EK, DK [52]uint16
}

type KeySizeError int

const BlockSize = 8
const MaxKeySize = 16

func MulInv(x uint16) uint16 {
	if x <= 1 {
		return x
	}
	var t1 uint16 = uint16(0x10001 / uint32(x))
	var y uint16 = uint16(0x10001 % uint32(x))
	if y == 1 {
		return (1 - t1)
	}
	var t0 uint16 = 1
	var q uint16
	for {
		q = x / y
		x = x % y
		t0 = t0 + (q * t1)
		if x == 1 {
			return t0
		}
		q = y / x
		y = y % x
		t1 = t1 + (q * t0)
		if y == 1 {
			break
		}
	}
	return (1 - t1)
}

func Mul(x *uint16, y uint16) {
	var p uint32 = uint32(*x) * uint32(y)
	if p == 0 {
		*x = 1 - *x - y
	} else {
		*x = uint16(p >> 16)
		var t16 uint16 = uint16(p & 0xffff)
		*x = t16 - *x
		if t16 < *x {
			*x += 1
		}
	}
}

func (k KeySizeError) Error() string {
	return "crypto/idea: invalid key size, it should be 128 bits at most"
}

func (c *Idea) BlockSize() int {
	return BlockSize
}

func CreateIdea(key []byte) (*Idea, error) {
	var c Idea
	if k := len(key); k == 0 || k > MaxKeySize { // CHECK ACTUAL BLOCKSIZE, TO FIX
		return nil, KeySizeError(k)
	}
	c.InitKey(key)
	return &c, nil
}

func (idea *Idea) InitKey(key []byte) {
	var i int = 0
	for ; 2*i+1 < len(key); i++ {
		idea.EK[i] = uint16(uint16(key[2*i]) + (uint16(key[2*i+1]) << 8))
	}
	for j := i; j < 52; j++ {
		idea.EK[j] = 0
	}
	for i := 0; i <= 7; i++ {
		idea.EK[i] = uint16((idea.EK[i] << 8) | (idea.EK[i] >> 8))
	}

	for i := 1; i <= 5; i++ {
		idea.EK[(i*8)+0] = uint16((idea.EK[((i-1)*8)+1] << 9) | (idea.EK[((i-1)*8)+2] >> 7))
		idea.EK[(i*8)+1] = uint16((idea.EK[((i-1)*8)+2] << 9) | (idea.EK[((i-1)*8)+3] >> 7))
		idea.EK[(i*8)+2] = uint16((idea.EK[((i-1)*8)+3] << 9) | (idea.EK[((i-1)*8)+4] >> 7))
		idea.EK[(i*8)+3] = uint16((idea.EK[((i-1)*8)+4] << 9) | (idea.EK[((i-1)*8)+5] >> 7))
		idea.EK[(i*8)+4] = uint16((idea.EK[((i-1)*8)+5] << 9) | (idea.EK[((i-1)*8)+6] >> 7))
		idea.EK[(i*8)+5] = uint16((idea.EK[((i-1)*8)+6] << 9) | (idea.EK[((i-1)*8)+7] >> 7))
		idea.EK[(i*8)+6] = uint16((idea.EK[((i-1)*8)+7] << 9) | (idea.EK[((i-1)*8)+0] >> 7))
		idea.EK[(i*8)+7] = uint16((idea.EK[((i-1)*8)+0] << 9) | (idea.EK[((i-1)*8)+1] >> 7))
	}

	idea.EK[48] = uint16((idea.EK[41] << 9) | (idea.EK[42] >> 7))
	idea.EK[49] = uint16((idea.EK[42] << 9) | (idea.EK[43] >> 7))
	idea.EK[50] = uint16((idea.EK[43] << 9) | (idea.EK[44] >> 7))
	idea.EK[51] = uint16((idea.EK[44] << 9) | (idea.EK[45] >> 7))

	idea.DK[51] = MulInv(idea.EK[3])
	idea.DK[50] = -idea.EK[2]
	idea.DK[49] = -idea.EK[1]
	idea.DK[48] = MulInv(idea.EK[0])
	for i := 0; i <= 6; i++ {
		idea.DK[47-i*6] = idea.EK[i*6+5]
		idea.DK[46-i*6] = idea.EK[i*6+4]
		idea.DK[45-i*6] = MulInv(idea.EK[i*6+9])
		idea.DK[44-i*6] = -idea.EK[i*6+7]
		idea.DK[43-i*6] = -idea.EK[i*6+8]
		idea.DK[42-i*6] = MulInv(idea.EK[i*6+6])
	}
	idea.DK[5] = idea.EK[47]
	idea.DK[4] = idea.EK[46]
	idea.DK[3] = MulInv(idea.EK[51])
	idea.DK[2] = -idea.EK[50]
	idea.DK[1] = -idea.EK[49]
	idea.DK[0] = MulInv(idea.EK[48])
}

func (idea *Idea) Encrypt(dst, src []byte) {
	var x [5]uint16

	x[1] = uint16((uint16(src[1]) << 8) + uint16(src[0]))
	x[2] = uint16((uint16(src[3]) << 8) + uint16(src[2]))
	x[3] = uint16((uint16(src[5]) << 8) + uint16(src[4]))
	x[4] = uint16((uint16(src[7]) << 8) + uint16(src[6]))

	for i := 1; i <= 4; i++ {
		x[i] = uint16((x[i] << 8) | (x[i] >> 8))
	}

	var s2, s3 uint16
	for i := 0; i <= 7; i++ {
		Mul(&x[1], idea.EK[(i*6)+0])
		x[2] += idea.EK[(i*6)+1]
		x[3] += idea.EK[(i*6)+2]
		Mul(&x[4], idea.EK[(i*6)+3])
		s3 = x[3]
		x[3] = x[3] ^ x[1]
		Mul(&x[3], idea.EK[(i*6)+4])
		s2 = x[2]
		x[2] = x[2] ^ x[4]
		x[2] += x[3]
		Mul(&x[2], idea.EK[(i*6)+5])
		x[3] += x[2]
		x[1] = x[1] ^ x[2]
		x[4] = x[4] ^ x[3]
		x[2] = x[2] ^ s3
		x[3] = x[3] ^ s2
	}
	Mul(&x[1], idea.EK[48])
	x[3] += idea.EK[49]
	x[2] += idea.EK[50]
	Mul(&x[4], idea.EK[51])
	x[1] = (x[1] << 8) | (x[1] >> 8)
	s2 = (x[3] << 8) | (x[3] >> 8)
	x[3] = (x[2] << 8) | (x[2] >> 8)
	x[4] = (x[4] << 8) | (x[4] >> 8)
	x[2] = s2

	dst[0] = byte(x[1] & 0xff)
	dst[1] = byte((x[1] >> 8) & 0xff)
	dst[2] = byte(x[2] & 0xff)
	dst[3] = byte((x[2] >> 8) & 0xff)
	dst[4] = byte(x[3] & 0xff)
	dst[5] = byte((x[3] >> 8) & 0xff)
	dst[6] = byte(x[4] & 0xff)
	dst[7] = byte((x[4] >> 8) & 0xff)
	return
}

func (idea *Idea) Decrypt(dst, src []byte) {
	var x [5]uint16

	x[1] = uint16((uint16(src[1]) << 8) + uint16(src[0]))
	x[2] = uint16((uint16(src[3]) << 8) + uint16(src[2]))
	x[3] = uint16((uint16(src[5]) << 8) + uint16(src[4]))
	x[4] = uint16((uint16(src[7]) << 8) + uint16(src[6]))

	for i := 1; i <= 4; i++ {
		x[i] = (x[i] << 8) | (x[i] >> 8)
	}

	var s2, s3 uint16
	for i := 0; i < 8; i++ {
		Mul(&x[1], idea.DK[(i*6)+0])
		x[2] += idea.DK[(i*6)+1]
		x[3] += idea.DK[(i*6)+2]
		Mul(&x[4], idea.DK[(i*6)+3])
		s3 = x[3]
		x[3] = x[3] ^ x[1]
		Mul(&x[3], idea.DK[(i*6)+4])
		s2 = x[2]
		x[2] = x[2] ^ x[4]
		x[2] += x[3]
		Mul(&x[2], idea.DK[(i*6)+5])
		x[3] += x[2]
		x[1] = x[1] ^ x[2]
		x[4] = x[4] ^ x[3]
		x[2] = x[2] ^ s3
		x[3] = x[3] ^ s2
	}
	Mul(&x[1], idea.DK[48])
	x[3] += idea.DK[49]
	x[2] += idea.DK[50]
	Mul(&x[4], idea.DK[51])
	x[1] = (x[1] << 8) | (x[1] >> 8)
	s2 = (x[3] << 8) | (x[3] >> 8)
	x[3] = (x[2] << 8) | (x[2] >> 8)
	x[4] = (x[4] << 8) | (x[4] >> 8)
	x[2] = s2

	dst[0] = byte(x[1] & 0xff)
	dst[1] = byte((x[1] >> 8) & 0xff)
	dst[2] = byte(x[2] & 0xff)
	dst[3] = byte((x[2] >> 8) & 0xff)
	dst[4] = byte(x[3] & 0xff)
	dst[5] = byte((x[3] >> 8) & 0xff)
	dst[6] = byte(x[4] & 0xff)
	dst[7] = byte((x[4] >> 8) & 0xff)
}
