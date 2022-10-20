//{ Driver Code Starts
//Initial Template for C


#include <stdio.h>

// } Driver Code Ends
//User function Template for C

void toBinary(int N)
{
    // your code here
    int a[256];
    int start=0;
    while (N!=0){
        a[start]=(N%2);
        start+=1;
        //printf("%d",N%2);
        N/=2;
        
    }
    for(int i=start-1;i>-1;i--)
    {
        printf("%d",a[i]);
    }
        
}

//{ Driver Code Starts.

int main() {
	//code
	
	int t;
	scanf("%d", &t);
	
	
	while(t--)
	{
	    int n;
	    scanf("%d", &n);
	    
	    toBinary(n);
	    printf("\n");
	}
	return 0;
}
// } Driver Code Ends