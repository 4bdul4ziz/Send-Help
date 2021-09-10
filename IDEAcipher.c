#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <time.h>
#include <stdbool.h>
#include "CipherModes_v1.h"

typedef unsigned int128 uint128_t;

uint64_t CodeTimer(bool startstop);


/* 
 * main
 * description: 
 *  will call the different ciphermodes of IDEA and time them
 * inputs:
 *  none
 * returns:
 *  will write results to file
 *
 */	
int main(int argc, char **argv) {

  uint64_t i;
  bool ENCRYPT=true, DECRYPT=false;
  uint64_t numtexts = 4;
  uint64_t plaintexts[4]={0x3003150030031500, 0xaaaaffff88890177, 0x3003150030031500, 0xaaaaffff88890177}, ciphertexts[4]={}, decodetexts[4]={};
  uint64_t initialvector = 0xBBBBCCCC44442222;
  uint128_t key = (((uint128_t)0xabcdabcdabcdabcd)<<64)+0xabcdabcdabcdabcd;
  
  // call ECB mode
  printf("\nEBC mode\n");
  Cipher_IDEA_Mode_ECB(ENCRYPT, key, numtexts, plaintexts, ciphertexts);
  Cipher_IDEA_Mode_ECB(DECRYPT, key, numtexts, ciphertexts, decodetexts);
  for(i = 0; i < 4; i++) {
  	printf("plaintext: %.16lx, ciphertext: %.16lx, decodetext: %.16lx\n", plaintexts[i], ciphertexts[i], decodetexts[i]); 
  }
  
  // call CBC mode
  printf("\nCBC mode\n");
  Cipher_IDEA_Mode_CBC(ENCRYPT, key, initialvector, numtexts, plaintexts, ciphertexts);
  Cipher_IDEA_Mode_CBC(DECRYPT, key, initialvector, numtexts, ciphertexts, decodetexts);
  for(i = 0; i < 4; i++) {
  	printf("plaintext: %.16lx, ciphertext: %.16lx, decodetext: %.16lx\n", plaintexts[i], ciphertexts[i], decodetexts[i]); 
  }
  
  // call CFB mode
  printf("\nCFB mode\n");
  Cipher_IDEA_Mode_CFB(ENCRYPT, key, initialvector, numtexts, plaintexts, ciphertexts);
  Cipher_IDEA_Mode_CFB(DECRYPT, key, initialvector, numtexts, ciphertexts, decodetexts);
  for(i = 0; i < 4; i++) {
  	printf("plaintext: %.16lx, ciphertext: %.16lx, decodetext: %.16lx\n", plaintexts[i], ciphertexts[i], decodetexts[i]); 
  }
  
  // call CTR mode
  printf("\nCTR mode\n");
  Cipher_IDEA_Mode_CTR(ENCRYPT, key, initialvector, numtexts, plaintexts, ciphertexts);
  Cipher_IDEA_Mode_CTR(DECRYPT, key, initialvector, numtexts, ciphertexts, decodetexts);
  for(i = 0; i < 4; i++) {
  	printf("plaintext: %.16lx, ciphertext: %.16lx, decodetext: %.16lx\n", plaintexts[i], ciphertexts[i], decodetexts[i]); 
  }
  
  return 0;
}

/*
 * CodeTimer
 * description:
 * 	function will time code execution in number of clock cycles
 * inputs:
 * 	startstop: 1 to start timer, 0 to stop timer
 * returns: 
 *  0 if sucessful start, -1 if unsuccesful start or stop, time value in ms if sucessful stop
 */
uint64_t CodeTimer(bool startstop) {
	static uint64_t prevTime;
	static bool running = 0;

	// if not running and start is requested start timer
	if(startstop == 1 && running == 0) {
		running = 1;
		prevTime = clock();
		return 0;
	// if running and stop is requested return time
	} else if(startstop == 0 && running == 1) {
		running = 0;
		return clock() - prevTime;
	// return -1 for non-valid cases	
	} else {
		return -1;
	}

}