        #include<stdio.h>
        #define MAX 20
        void main()
        {
          int a[MAX];
          int n,i,j=0,max,smax;
          printf("Enter number of elements\n");
          scanf("%d",&n);
          printf("Enter the elements:\n");
          for(i=0;i<n;i++)
          {
           scanf("%d",&a[i]);
          }
          max=a[0];
          for(i=1;i<n;i++)
          {
           if(max<a[i])
           {
            max=a[i];
            j=i;
           }
          }
          smax=a[n-j-1];
          for(i=1;i<n;i++)
          {
           if(smax<a[i] && j!=i)
            smax=a[i];
          }
          printf("Second biggest element: %d", smax);
         return 0;
        }
