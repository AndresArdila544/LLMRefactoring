#include <stdio.h>
#include <math.h>
int main()
{
    int i,j=0;
    float n1[5],n2[5];

    for(i=0;i<3;++i)
    {
        scanf("%f %f",&n1[i],&n2[i]);
    }
    do
    {
        j++;
        printf("\n");
        if(n2[j]==0 && n1[j]==0)
            break;
        printf("Case 1:%d\n",j);
    }while(n2[j]!=0 || n1[j]!=0);
    return 0;
}


#include <stdio.h>
int main()
{
    int i=0,j=0,s=0,k=0,l=0,m=0,sum=0,a[2];
    scanf("%d %d",&i,&j);
    do
    {
        for(k=1; k<i+1; ++k)
            for(l=k+1; l<i+1; ++l)
                for(m=l+1; m<i+1; ++m)
                    if((sum=k+l+m)==j)
                        s++;
        printf("%d\n",s);
        sum = 0, k=0, l=0, m=0, s=0;
        scanf("%d %d",&i,&j);
    }while(j!=0 || i!=0);
}


#include <stdio.h>
int main()
{
    int i=1;
    do
    {
        printf("Case 1:%d\n",i++);
        if(scanf("%d %d",&i,&i)!=2)
            break;
    }while((i||0));
}