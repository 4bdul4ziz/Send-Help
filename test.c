#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <sys/wait.h>

void prio_sc(int process[10], int burst_time[10], int wait_time[10], int priority[10], int turnar_time[10], int n, float avg_wt, float avg_tat)
{
   int temp, flag;
   int total = 0;
   for (int i = 0; i < n; i++)
   {
      flag = i; //position counter
      for (int j = i + 1; j < n; j++)
      {
         if (priority[j] < priority[flag])
         { //sorting on basis of priority
            flag = j;
         }
      }

      temp = priority[i];
      priority[i] = priority[flag];
      priority[flag] = temp;

      temp = burst_time[i];
      burst_time[i] = burst_time[flag];
      burst_time[flag] = temp;

      temp = process[i];
      process[i] = process[flag];
      process[flag] = temp;
   }
   wait_time[0] = 0; //for 1st process waiting time=0
   for (int i = 1; i < n; i++)
   {
      wait_time[i] = 0;
      for (int j = 0; j < n; j++)
      {
         wait_time[i] += burst_time[j];
      }

      total += wait_time[i];
   }

   avg_wt = total / n;

   total = 0;
   for (int i = 0; i < n; i++)
   {
      turnar_time[i] = burst_time[i] + wait_time[i];
      total += turnar_time[i];
   }
   avg_tat = total / n;
   printf("average turnaround : %f", avg_tat);
   printf("\naverage wait : %f", avg_wt);
}

int main()
{
   int process[10], burst_time[10], priority[10], wait_time[10], turnar_time[10];
   float avg_wt = 0, avg_tat = 0;
   int n;
   srand(time(0));
   printf("Enter number of processes: ");
   scanf("%d", &n);

   for (int i = 0; i < n; i++)
   {
      printf("Priority: ");
      scanf("%d", &priority[i]);
      process[i] = i + 1; //Process number
   }

   for (int i = 0; i < n; i++)
   {
      burst_time[i] = rand() % 15 + 1; //generating random burst times for each process
   }

   prio_sc(process, burst_time, wait_time, priority, turnar_time, n, avg_wt, avg_tat);

   printf("\nProcess\t Burst time\t Waiting time\t Turnaround time\n");
   for (int i = 0; i < n; i++)
   {
      printf("%d\t\t%d\t\t%d\t\t%d\n", process[i], burst_time[i], wait_time[i], turnar_time[i]);
   }
   printf("\n");
   printf("\nThe average waiting time is : %f", avg_wt);
   printf("\nThe average turnaround time is : %f", avg_tat);
   printf("\n");
   return 0;
}