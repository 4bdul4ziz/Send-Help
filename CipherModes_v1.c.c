
#include "CipherModes_v1.h"

/*
 * Cipher_IDEA_Mode_EBC
 * description:
 *  Performs IDEA cipher decryption and encryption in ECB mode (basic mode) where one
 *  key encrypts all plaintext blocks. This mode is deterministic and very
 *  insecure.
 * inputs:
 *  modeselect: (bool) if 1 then encryption, if 0 then decryption occurs
 *  key: (uint128_t) a 128 bit key
 *  numtexts: (uint64_t) the number of texts to be encrypted or decrypted (see modeselect)
 *  intexts: (*uint64_t) a list of texts to be encrypted or decrypted (see modeselect)
 *  outtexts: (*uint64_t) the output of encryption or decryption needs to be allocated for a least
 *            as much space as intexts
 * output:
 *  returns the requested encryption or decryption of intexts in outtexts
 *  
 */
void Cipher_IDEA_Mode_ECB(bool modeselect, uint128_t key, uint64_t numtexts, uint64_t *intexts, uint64_t *outtexts) {
	uint64_t i;
	uint16_t *key_encrypt, *key_decrypt;
	
	// allocate memory for round keys and generate round keys
	key_encrypt = (uint16_t*) malloc(sizeof(uint16_t) * 54);
	key_decrypt = (uint16_t*) malloc(sizeof(uint16_t) * 54);
	Key_Generator(key, key_encrypt, key_decrypt);
	
	// perform ECB encryption/decryption
	for(i = 0; i < numtexts; i++) {
		if(modeselect) { // if 1 then encrypt
			outtexts[i] = Cipher_IDEA_encryptdecrypt(intexts[i], key_encrypt, 0);
		} else { // else decrypt
			outtexts[i] = Cipher_IDEA_encryptdecrypt(intexts[i], key_decrypt, 0);
		}
	}
}

/*
 * Cipher_IDEA_Mode_CBC
 * description:
 *  Performs IDEA cipher decryption and encryption in CBC mode where one
 *  key encrypts all plaintext blocks and the plaintexts are xor'd with the previous output. 
 * inputs:
 *  modeselect: (bool) if 1 then encryption, if 0 then decryption occurs
 *  key: (uint128_t) a 128 bit key
 *  initialvector: (uint64_t) a 64 bit initial value to xor with the first plaintext
 *  numtexts: (uint64_t) the number of texts to be encrypted or decrypted (see modeselect)
 *  intexts: (*uint64_t) a list of texts to be encrypted or decrypted (see modeselect)
 *  outtexts: (*uint64_t) the output of encryption or decryption needs to be allocated for a least
 *            as much space as intexts
 * output:
 *  returns the requested encryption or decryption of intexts in outtexts
 *  
 */
void Cipher_IDEA_Mode_CBC(bool modeselect, uint128_t key, uint64_t initialvector, uint64_t numtexts, uint64_t *intexts, uint64_t *outtexts) {
	uint64_t i;
	uint16_t *key_encrypt, *key_decrypt;
	
	// allocate memory for round keys and generate round keys
	key_encrypt = (uint16_t*) malloc(sizeof(uint16_t) * 54);
	key_decrypt = (uint16_t*) malloc(sizeof(uint16_t) * 54);
	Key_Generator(key, key_encrypt, key_decrypt);
	
	// perform CBC encryption/decryption
	if(modeselect) { // if 1 then encrypt
		outtexts[0] = Cipher_IDEA_encryptdecrypt(intexts[0] ^ initialvector, key_encrypt, 0);
	} else { // else decrypt
		outtexts[0] = initialvector ^ Cipher_IDEA_encryptdecrypt(intexts[0], key_decrypt, 0);
	}
	for(i = 1; i < numtexts; i++) {
		if(modeselect) { // if 1 then encrypt
			outtexts[i] = Cipher_IDEA_encryptdecrypt(intexts[i] ^ outtexts[i-1], key_encrypt, 0);
		} else { // else decrypt
			outtexts[i] = intexts[i-1] ^ Cipher_IDEA_encryptdecrypt(intexts[i], key_decrypt, 0);
		}
	}
}

/*
 * Cipher_IDEA_Mode_CFB
 * description:
 *  Performs IDEA cipher decryption and encryption in CFB mode.
 * inputs:
 *  modeselect: (bool) if 1 then encryption, if 0 then decryption occurs
 *  key: (uint128_t) a 128 bit key
 *  initialvector: (uint64_t) a 64 bit initial value to xor with the first plaintext
 *  numtexts: (uint64_t) the number of texts to be encrypted or decrypted (see modeselect)
 *  intexts: (*uint64_t) a list of texts to be encrypted or decrypted (see modeselect)
 *  outtexts: (*uint64_t) the output of encryption or decryption needs to be allocated for a least
 *            as much space as intexts
 * output:
 *  returns the requested encryption or decryption of intexts in outtexts
 *  
 */
void Cipher_IDEA_Mode_CFB(bool modeselect, uint128_t key, uint64_t initialvector, uint64_t numtexts, uint64_t *intexts, uint64_t *outtexts) {
	uint64_t i;
	uint16_t *key_encrypt, *key_decrypt;
	
	// allocate memory for round keys and generate round keys
	key_encrypt = (uint16_t*) malloc(sizeof(uint16_t) * 54);
	key_decrypt = (uint16_t*) malloc(sizeof(uint16_t) * 54);
	Key_Generator(key, key_encrypt, key_decrypt);
	
	// perform CFB encryption/decryption
	if(modeselect) { // if 1 then encrypt
		outtexts[0] = intexts[0] ^ Cipher_IDEA_encryptdecrypt(initialvector, key_encrypt, 0);
	} else { // else decrypt
		outtexts[0] = intexts[0] ^ Cipher_IDEA_encryptdecrypt(initialvector, key_encrypt, 0);
	}
	for(i = 1; i < numtexts; i++) {
		if(modeselect) { // if 1 then encrypt
			outtexts[i] = intexts[i] ^ Cipher_IDEA_encryptdecrypt(outtexts[i-1], key_encrypt, 0);
		} else { // else decrypt
			outtexts[i] = intexts[i] ^ Cipher_IDEA_encryptdecrypt(intexts[i-1], key_encrypt, 0);
		}
	}
}

/*
 * Cipher_IDEA_Mode_OFB
 * description:
 *  Performs IDEA cipher decryption and encryption in OFB mode.
 * inputs:
 *  modeselect: (bool) if 1 then encryption, if 0 then decryption occurs note modeselect actually
 *              does nothing just helpful for notation
 *  key: (uint128_t) a 128 bit key
 *  initialvector: (uint64_t) a 64 bit initial value to xor with the first plaintext
 *  numtexts: (uint64_t) the number of texts to be encrypted or decrypted (see modeselect)
 *  intexts: (*uint64_t) a list of texts to be encrypted or decrypted (see modeselect)
 *  outtexts: (*uint64_t) the output of encryption or decryption needs to be allocated for a least
 *            as much space as intexts
 * output:
 *  returns the requested encryption or decryption of intexts in outtexts
 *  
 */
void Cipher_IDEA_Mode_OFB(bool modeselect, uint128_t key, uint64_t initialvector, uint64_t numtexts, uint64_t *intexts, uint64_t *outtexts) {
	uint64_t i;
	uint16_t *key_encrypt, *key_decrypt;
	uint64_t *temptexts;
	
	// allocate memory for round keys and generate round keys
	key_encrypt = (uint16_t*) malloc(sizeof(uint16_t) * 54);
	key_decrypt = (uint16_t*) malloc(sizeof(uint16_t) * 54);
	Key_Generator(key, key_encrypt, key_decrypt);
	
	// allocate memory for temptexts 
	temptexts = (uint64_t*) malloc(sizeof(uint64_t) * numtexts); 
	
	// perform CFB encryption/decryption
	temptexts[0] = Cipher_IDEA_encryptdecrypt(initialvector, key_encrypt, 0);
	outtexts[0] = intexts[0] ^ temptexts[0];
	
	for(i = 1; i < numtexts; i++) {
		outtexts[i] = intexts[i] ^ Cipher_IDEA_encryptdecrypt(temptexts[i-1], key_encrypt, 0);
	}
}

/*
 * Cipher_IDEA_Mode_CTR
 * description:
 *  Performs IDEA cipher decryption and encryption in CTR mode which turns any block cipher
 *  into a stream cipher.
 * inputs:
 *  modeselect: (bool) if 1 then encryption, if 0 then decryption occurs **note modeselect actually
 *              does nothing just helpful for notation
 *  key: (uint128_t) a 128 bit key
 *  initialvector: (uint64_t) a 64 bit initial value to xor with the first plaintext
 *  numtexts: (uint64_t) the number of texts to be encrypted or decrypted (see modeselect)
 *  intexts: (*uint64_t) a list of texts to be encrypted or decrypted (see modeselect)
 *  outtexts: (*uint64_t) the output of encryption or decryption needs to be allocated for a least
 *            as much space as intexts
 * output:
 *  returns the requested encryption or decryption of intexts in outtexts
 *  
 */
void Cipher_IDEA_Mode_CTR(bool modeselect, uint128_t key, uint64_t initialvector, uint64_t numtexts, uint64_t *intexts, uint64_t *outtexts) {
	uint64_t i;
	uint16_t *key_encrypt, *key_decrypt;
	
	// allocate memory for round keys and generate round keys
	key_encrypt = (uint16_t*) malloc(sizeof(uint16_t) * 54);
	key_decrypt = (uint16_t*) malloc(sizeof(uint16_t) * 54);
	Key_Generator(key, key_encrypt, key_decrypt);

	// perform CFB encryption/decryption
	for(i = 0; i < numtexts; i++) {
		outtexts[i] = intexts[i] ^ Cipher_IDEA_encryptdecrypt(initialvector ^ i, key_encrypt, 0);
	}
}

/*
 * Cipher_IDEA_encryptdecrypt
 * description:
 * 	function is capable of encryption and decryption with only changes to roundkeys needed
 * inputs:
 * 	plaintext: the block of data to be encrypted or decrypted
 * 	K: a pointer to a list of 54 cipher keys (initial key of 128bits should contain very few zeros) (pass encry)
 *     use encryption keys for encryption and decryption keys for decryption
 *  offset: for debugging use default to 0 for normal use
 * returns: 
 *  the cyphertext of the original plaintext after $rounds number of rounds
 */
uint64_t Cipher_IDEA_encryptdecrypt(uint64_t plaintext, uint16_t *K, uint16_t offset) {
    // split plaintext into 4 16bit parts 
    uint16_t a=(plaintext & 0xFFFF000000000000) >> 48, b=(plaintext & 0x0000FFFF00000000) >> 32,
        c=(plaintext & 0x00000000FFFF0000) >> 16, d=(plaintext & 0x000000000000FFFF) >> 0;
	
    // declare scratch variables
    uint64_t ciphertext;
    uint16_t e = 0, f = 0;
    uint16_t i;
    uint16_t *k;
    
    //Point to the key schedule
  	k = K+offset;
  	uint16_t rounds = 8;
    
    for(i = 0; i < rounds; i++)
    {
       //printf("encode %d: a: %.4x, b: %.4x, c: %.4x, d: %.4x\n", i,a,b,c,d);
       //Apply a round
       a = ideaMul(a, k[0]); //good
       b += k[1]; //good
       c += k[2]; //good
       d = ideaMul(d, k[3]); //good
 		
  	   //printf("          a: %.4x, b: %.4x, c: %.4x, d: %.4x\n", a,b,c,d); 
       e = a ^ b; // right here is the error in example code they do
       f = c ^ d; // a^c and b^d which is an error because we should swap
 	   //printf("          e: %.4x, f: %.4x\n", e, f); 
       //e = ideaMul(e, k[4]); // to call this the new value of e or to say f += ideaMul(k[4], e);?
       e = ideaMul(e, 46457);
       f += e;
       //f = ideaMul(f,k[5]);
       f = ideaMul(f,46457);
       e += f;
 	   
 	   //printf("          e: %.4x, f: %.4x\n", e, f);
 	   //f = 0x88ff, e = 0x0224; 
       a ^= f;//good
       d ^= e;//good
       //e ^= b;
       //f ^= c;
 
       b = f^b; // good
       c = e^c; // good
       if(i < rounds-1) { 
       		uint16_t temp = c; // good
       		c = b; // good
       		b = temp; // good
       }
  	   //printf("          a: %.4x, b: %.4x, c: %.4x, d: %.4x\n", a,b,c,d); 
       //Advance current location in key schedule
       k += 6;
       

    }
 
    //The four 16-bit values produced at the end of the 8th encryption
    //round are combined with the last four of the 52 key sub-blocks
    //if(offset != 0) { //clearly shows that the following section is correct!
    //	a = 0x532f; b = 0xc0cd; c = 0xdbd0; d = 0xc2e9;
    //}
    a = ideaMul(a, k[0]);//good
    c += k[1]; //good
    b += k[2]; //good
  	d = ideaMul(d, k[3]);//good
  	
  	//printf("encode %d: a: %.4x, b: %.4x, c: %.4x, d: %.4x\n", 8,a,b,c,d);
  	
  	ciphertext = 0;
  	ciphertext = (ciphertext | a) << 16;
    ciphertext = (ciphertext | b) << 16;
    ciphertext = (ciphertext | c) << 16;
    ciphertext = (ciphertext | d) << 0;

    return (ciphertext);  
}

/*
 * Key_Generator
 * description:
 * 	function is capable of generating arrays (16bit x 52) of encryption and decryption keys
 * inputs:
 * 	IDEAkey: initial 128bit key used to generate key arays
 * 	encrypt: a pointer to the encrypt key list
 *  decrypt: a pointer to the decrypt key list
 * returns: 
 *  NULL
 */
void Key_Generator(uint128_t IDEAkey, uint16_t *encrypt, uint16_t *decrypt) {
	int i=0;
    // Generate encryption keys 1-48
    while(i < 52) {
        encrypt[i] = (IDEAkey >> 112); 
    	encrypt[i+1] = (IDEAkey >> 80); 
    	encrypt[i+2] = (IDEAkey >> 96); 
    	encrypt[i+3] = (IDEAkey >> 64); 
    	encrypt[i+4] = (IDEAkey >> 48); 
    	encrypt[i+5] = (IDEAkey >> 32);
    	encrypt[i+6] = (IDEAkey >> 16);
    	encrypt[i+7] = (IDEAkey >> 0);   
    	i += 8;
        IDEAkey = (IDEAkey << 25) | (IDEAkey >> (sizeof(IDEAkey)*8 - 25));
    }
    
    // keys 49-52
    encrypt[i] = (IDEAkey >> 112); //K49
    encrypt[i+1] = (IDEAkey >> 80); //K51
    encrypt[i+2] = (IDEAkey >> 96); //K50
    encrypt[i+3] = (IDEAkey >> 64); //K52
   
    //encrypt = encrypt - 52;
	for(i = 0; i < 52; i+=6) {
		decrypt[i] = ideaInv(encrypt[48-i]);
 
		if(i == 0 || i == 48) { // flip because first and last 4 keys
			decrypt[i + 1] = -encrypt[49 - i];
		    decrypt[i + 2] = -encrypt[50 - i];
		} else { // otherwise don't flip
		    decrypt[i + 1] = -encrypt[50 - i];
		    decrypt[i + 2] = -encrypt[49 - i];
		}
		
		decrypt[i + 3] = ideaInv(encrypt[51 - i]);
		
		if(i < 48) {
		    decrypt[i + 4] = encrypt[46 - i];
		    decrypt[i + 5] = encrypt[47 - i];
	    }
	}
}

/*
 * ideaMul
 * Description:
 *  will return the special IDEA multiplication where 0x0000 is treated as 0xFFFF
 * inputs:
 *  a,b: the two numbers to be multiplied
 * outputs:
 *  returns special IDEA multiplication
 *
 */
static uint16_t ideaMul(uint16_t a, uint16_t b) {
   uint32_t c = a * b;
   if(c) {
      c = (ROL32(c,16) - c) >> 16;
      return (c + 1) & 0xFFFF;
   } else {
      return (1 - a - b) & 0xFFFF;
   }
}
 
/*
 * ideaInv
 * Description:
 *  will return the special IDEA modulo inverse where 0x0000 is treated as 0xFFFF
 * inputs:
 *  a: the number to be inverted
 * outputs:
 *  returns special IDEA modulo inverse
 *
 */
static uint16_t ideaInv(uint16_t a) {
   uint32_t b;
   uint32_t q;
   uint32_t r;
   int32_t t;
   int32_t u;
   int32_t v;
   b = 0x10001;
   u = 0;
   v = 1;
   while(a > 0) {
      q = b / a;
      r = b % a;
      b = a;
      a = r;
      t = v;
      v = u - q * v;
      u = t;
   }
   if(u < 0) {
      u += 0x10001;
   }
   return u;
}