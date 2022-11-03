#include <iostream>
#include <math.h>
using namespace std;
int factorize(long long n){
   int mul=1,extra=0;
   int count = 0;
   while (!(n % 2)) {
      n/= 2;
      count++;
   }
   if (count)
      mul=mul*2;
   for (long long i = 3; i <= sqrt(n); i += 2) {
      count = 0;
      while (n % i == 0) {
         count++;
         n = n / i;
      }
      if (count)
        mul=mul*i;
      if(count%2==1){
          count++;
          if(count==1)
            extra=extra+1;
          extra=extra+count%2;
      }
      else{
          extra=extra+count%2;
      }
   }
   if (n > 2){
      mul=mul*n;
      extra=extra+count;
   }
   cout<<extra<<endl;
   mul=mul+extra;
   return mul;
}
int main() {
   long long N;
   cin>>N;
   int ans;
   ans=factorize(N);
   cout<<endl;
   cout<<ans;
   return 0;
}