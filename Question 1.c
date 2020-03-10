/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int test_case;
    int a;
    int b;
    int k;

    int answer[100];
    int i;
    int l;
    
    scanf("%d", &test_case);
    
    if (test_case<=100) {
        for (l=0; l<test_case; l++) {
            scanf("%d", &a);
            scanf("%d", &b);
            scanf("%d", &k);
            
            answer[l]=0;
            for (i = a; i <= b; ++i) {
                if ( i % k == 0){
                    answer[l]++;
                }
            }
        }
    }
    
    for (l=0; l<test_case; l++) {
        printf("Case %d: %d\n", l+1, answer[l]);
    } 
        
    return 0;
}
