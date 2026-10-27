import os
from flask import Flask, Response

app = Flask(__name__)

@app.route('/<exp_code>', methods=['GET'])
def get_experiment_code(exp_code):
    match exp_code:
        case "exp1":
            # Selection Sort[cite: 27]
            code = r"""#include<stdio.h>
#include<conio.h>
void main(){
int arr[]={75,55,5,1,16};
int i,j,minj,minx;
clrscr();
for(i=0;i<5;i++){
minj=i;
minx=arr[i];
for(j=i+1;j<5;j++){
if(arr[j]<minx){
minj=j;
minx=arr[j];
}
}
arr[minj]=arr[i];
arr[i]=minx;
}
printf("Sorted array by using Selection sort:");
for(i=0;i<5;i++){
printf("\t%d",arr[i]);
}
getch();
}"""

        case "exp2":
            # Insertion Sort[cite: 26]
            code = r"""#include <stdio.h>
#include <conio.h>
void main()
{
    int a[5] = {75,55,5,1,16};
    int i, j, key;
    clrscr();
    for(i = 1; i < 5; i++)
    {
        key = a[i];
        j = i - 1;
        while(j >= 0 && a[j] > key)
        {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
    printf("Sorted array using Insertion Sort: ");
    for(i = 0; i < 5; i++)
    {
        printf("%d ", a[i]);
    }
    getch();
}"""

        case "exp3":
            # Binary Search Algorithm[cite: 25]
            code = r"""#include<stdio.h>
#include<conio.h>
void main()
{   int i;
    int A[5] = {10,20,30,40,50};
    int key, low, high, mid;
    clrscr();
    printf("Array is:");
    for(i=0;i<5;i++){
    printf("\t%d",A[i]);
    }
    printf("\nEnter key: ");
    scanf("%d",&key);
    low = 0;
    high = 4;
    while(low <= high)
    {
        mid = (low + high) / 2;
        if(A[mid] == key)
        {
            printf("\nElement found at position %d", mid);
            getch();
            return;
        }
        else if(A[mid] < key)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    printf("\nElement not found");
    getch();
}"""

        case "exp4":
            # Quick Sort[cite: 24]
            code = r"""#include <stdio.h>
#include <conio.h>
void quicksort(int a[], int low, int high)
{
    int i, j, pivot, temp;
    if (low < high)
    {
        pivot = a[low];
        i = low;
        j = high;
        while (i < j)
        {
            while (a[i] <= pivot && i < high)
                i++;
            while (a[j] > pivot)
                j--;
            if (i < j)
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
        temp = a[low];
        a[low] = a[j];
        a[j] = temp;
        quicksort(a, low, j - 1);
        quicksort(a, j + 1, high);
    }
}
void main()
{
    int a[50], n, i;
    clrscr();
    printf("Enter number of elements: ");
    scanf("%d", &n);
    printf("Enter elements:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    quicksort(a, 0, n - 1);
    printf("Sorted array:\n");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    getch();
}"""

        case "exp5":
            # Fractional Knapsack[cite: 23]
            code = r"""#include <stdio.h>
#include <conio.h>
struct item
{
    int weight;
    int profit;
    float ratio;
};
void main()
{
    struct item a[20], temp;
    int n, capacity, i, j;
    float profit = 0, fraction;
    clrscr();
    printf("Enter number of items: ");
    scanf("%d", &n);
    printf("\nEnter weight and profit:\n");
    for(i = 0; i < n; i++)
    {
        printf("Item %d: ", i + 1);
        scanf("%d%d", &a[i].weight, &a[i].profit);
        a[i].ratio = (float)a[i].profit / a[i].weight;
    }
    printf("\nEnter capacity: ");
    scanf("%d", &capacity);
    for(i = 0; i < n - 1; i++)
    {
        for(j = i + 1; j < n; j++)
        {
            if(a[i].ratio < a[j].ratio)
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
    printf("\nItems selected:\n");
    for(i = 0; i < n; i++)
    {
        if(capacity >= a[i].weight)
        {
            capacity = capacity - a[i].weight;
            profit = profit + a[i].profit;
            printf("Item %d\n", i + 1);
        }
        else
        {
            fraction = (float)capacity / a[i].weight;
            profit = profit + a[i].profit * fraction;
            if(fraction == 0.6666667)
                printf("2/3 of Item %d\n", i + 1);
            else
                printf("%.2f of Item %d\n", fraction, i + 1);
            break;
        }
    }
    printf("\nMaximum Profit = %.2f", profit);
    getch();
}"""

        case "exp6":
            # Job sequencing with deadline[cite: 22]
            code = r"""#include <stdio.h>
#include <conio.h>
struct job
{
    char id;
    int deadline;
    int profit;
};
void main()
{
    struct job a[20], temp;
    int n, i, j, k, maxd = 0;
    int slot[20];
    int totalProfit = 0;
    clrscr();
    printf("Enter number of jobs: ");
    scanf("%d", &n);
    printf("\nEnter job id, deadline and profit:\n");
    for(i = 0; i < n; i++)
    {
        scanf(" %c%d%d", &a[i].id, &a[i].deadline, &a[i].profit);
        if(a[i].deadline > maxd)
            maxd = a[i].deadline;
    }
    for(i = 0; i < n - 1; i++)
    {
        for(j = i + 1; j < n; j++)
        {
            if(a[i].profit < a[j].profit)
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
    for(i = 1; i <= maxd; i++)
        slot[i] = -1;
    for(i = 0; i < n; i++)
    {
        for(j = a[i].deadline; j >= 1; j--)
        {
            if(slot[j] == -1)
            {
                slot[j] = i;
                totalProfit = totalProfit + a[i].profit;
                break;
            }
        }
    }
    printf("\nJob Sequence: ");
    for(i = 1; i <= maxd; i++)
    {
        if(slot[i] != -1)
            printf("%c ", a[slot[i]].id);
    }
    printf("\nMaximum Profit = %d", totalProfit);
    getch();
}"""

        case "exp7":
            # All pair shortest Path (Floyd Warshall Algorithm)[cite: 21]
            code = r"""#include <stdio.h>
#include <conio.h>
#include <string.h>
#define INF 999
void main()
{
    int a[10][10], n, i, j, k;
    char x[10];
    clrscr();
    printf("Enter number of vertices: ");
    scanf("%d", &n);
    printf("\nEnter cost matrix:\n");
    printf("Enter INF for no direct path\n\n");
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            scanf("%s", x);
            if(strcmp(x, "INF") == 0)
                a[i][j] = INF;
            else
                a[i][j] = atoi(x);
        }
    }
    for(k = 0; k < n; k++)
    {
        for(i = 0; i < n; i++)
        {
            for(j = 0; j < n; j++)
            {
                if(a[i][k] + a[k][j] < a[i][j])
                    a[i][j] = a[i][k] + a[k][j];
            }
        }
    }
    printf("\nShortest Distance Matrix:\n\n");
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            if(a[i][j] >= INF)
                printf("INF\t");
            else
                printf("%d\t", a[i][j]);
        }
        printf("\n");
    }
    getch();
}"""

        case "exp8":
            # N-Queen problem[cite: 20]
            code = r"""#include <stdio.h>
#include <conio.h>
int board[20], rows, cols, queens;
int place(int row, int col)
{
    int i;
    for(i = 1; i < row; i++)
    {
        if(board[i] == col)
            return 0;
        if(board[i] - i == col - row)
            return 0;
        if(board[i] + i == col + row)
            return 0;
    }
    return 1;
}
void queen(int row)
{
    int col, i;
    for(col = 1; col <= cols; col++)
    {
        if(place(row, col))
        {
            board[row] = col;
            if(row == queens)
            {
                printf("\nSolution:\n");
                for(i = 1; i <= rows; i++)
                {
                    for(col = 1; col <= cols; col++)
                    {
                        if(board[i] == col)
                            printf("Q%d\t", i);
                        else
                            printf("-\t");
                    }
                    printf("\n");
                }
            }
            else
                queen(row + 1);
        }
    }
}
void main()
{
    clrscr();
    printf("Enter number of rows: ");
    scanf("%d", &rows);
    printf("Enter number of columns: ");
    scanf("%d", &cols);
    printf("Enter number of queens: ");
    scanf("%d", &queens);
    if(queens > rows || queens > cols)
    {
        printf("\nNo solution possible.");
    }
    else
    {
        queen(1);
    }
    getch();
}"""

        case "exp9":
            # Sum of Subset[cite: 19]
            code = r"""#include <stdio.h>
#include <conio.h>
int a[20], x[20], n, target;
void subset(int k, int sum)
{
    int i;
    if(sum == target)
    {
        printf("\nSubset: ");
        for(i = 0; i < n; i++)
        {
            if(x[i] == 1)
                printf("%d ", a[i]);
        }
        return;
    }
    if(k >= n || sum > target)
        return;
    x[k] = 1;
    subset(k + 1, sum + a[k]);
    x[k] = 0;
    subset(k + 1, sum);
}
void main()
{
    int i;
    clrscr();
    printf("Enter number of elements: ");
    scanf("%d", &n);
    printf("\nEnter elements:\n");
    for(i = 0; i < n; i++)
    {
        printf("Element %d: ", i + 1);
        scanf("%d", &a[i]);
    }
    printf("\nEnter target sum: ");
    scanf("%d", &target);
    printf("\nSubsets with sum %d:\n", target);
    subset(0, 0);
    getch();
}"""

        case "exp10":
            # Naïve String matching[cite: 18]
            code = r"""#include <stdio.h>
#include <string.h>
void naiveStringMatch(char text[], char pattern[]) {
    int n = strlen(text);
    int m = strlen(pattern);
    int matchFound = 0;
    for (int s = 0; s <= n - m; s++) {
        int j;
        for (j = 0; j < m; j++) {
            if (text[s + j] != pattern[j]) {
                break; 
            }
        }
        if (j == m) {
            printf("Pattern found at index: %d\n", s);
            matchFound = 1;
        }
    }
    if (!matchFound) {
        printf("Pattern not found in the given main string.\n");
    }
}
int main() {
    char text[] = "Raman";
    char pattern[] = "man";
    printf("Main String: \"%s\"\n", text);
    printf("Pattern:     \"%s\"\n\n", pattern);
    printf("Searching results:\n");
    naiveStringMatch(text, pattern);
    return 0;
}"""

        case _:
            code = "# Error: Experiment code not found. Available keys: exp1 through exp10."

    return Response(code, mimetype='text/plain')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
