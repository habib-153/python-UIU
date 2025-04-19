#include <stdio.h>

int main()
{
    int n, i, key, found = 0;
    scanf("%d", &n);

    int a[n];
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    scanf("%d", &key);
    
    printf("found at index position: ");
    
    for (i = 0; i < n; i++)
    {
        if (a[i] == key)
        {
            if (found == 0)
            {
                found = 1;
                printf("%d", i);
            }
            else
            {
                printf(", %d", i);
            }
        }
    }
    
    if (found)
    {
        printf("\n");
    }
    else
    {
        printf("not found\n");
    }

    return 0;
}