#ifndef CIPHERMODES_V1_H_
#define CIPHERMODES_V1_H_

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <inttypes.h>
#include <ctype.h> 
#include <time.h>
#include <stdbool.h>

typedef unsigned __int128 uint128_t;

#define ROL32(a,n) (((a) << (n)) | ((a) >> (32 - (n))))

void Cipher_IDEA_Mode_ECB(bool modeselect, uint128_t key, uint64_t numtexts, uint64_t *intexts, uint64_t *outtexts);
void Cipher_IDEA_Mode_CBC(bool modeselect, uint128_t key, uint64_t initialvector, uint64_t numtexts, uint64_t *intexts, uint64_t *outtexts);
void Cipher_IDEA_Mode_CFB(bool modeselect, uint128_t key, uint64_t initialvector, uint64_t numtexts, uint64_t *intexts, uint64_t *outtexts);
void Cipher_IDEA_Mode_OFB(bool modeselect, uint128_t key, uint64_t initialvector, uint64_t numtexts, uint64_t *intexts, uint64_t *outtexts);
void Cipher_IDEA_Mode_CTR(bool modeselect, uint128_t key, uint64_t initialvector, uint64_t numtexts, uint64_t *intexts, uint64_t *outtexts);

uint64_t Cipher_IDEA_encryptdecrypt(uint64_t plaintext, uint16_t *K, uint16_t offset);
void Key_Generator(uint128_t IDEAkey, uint16_t *encrypt, uint16_t *decrypt);
static uint16_t ideaMul(uint16_t a, uint16_t b);
static uint16_t ideaInv(uint16_t a);

#endif