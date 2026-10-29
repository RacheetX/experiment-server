
import os
from flask import Flask, Response

app = Flask(__name__)

@app.route('/<exp_code>', methods=['GET'])
def get_experiment_code(exp_code):
    match exp_code:
        case "exp1":
            # Experiment 1: Binary to Decimal and Octal to Binary Conversion[cite: 31, 32]
            code = r"""
// ==========================================
// CODE 1: Binary to Decimal
// ==========================================
#include<stdio.h>
#include<conio.h>
void main()
{
int binary, decimal = 0, base = 1, rem;
clrscr();
printf("Enter binary number: ");
scanf("%d", &binary);
while (binary > 0)
{
rem = binary % 10;
decimal = decimal + rem * base;
binary = binary / 10;
base = base * 2;
}
printf("Decimal number = %d", decimal);
getch();
}

// ==========================================
// CODE 2: Octal to Binary
// ==========================================
#include<stdio.h>
#include<conio.h>
void main()
{
int octal, temp;
int decimal = 0, base = 1;
int binary [50], i = 0, rem;
clrscr();
printf("\nEnter an octal number = ");
scanf("%d", &octal);
temp = octal;
while (temp > 0)
/* octal -> decimal */
{
rem = temp % 10;
decimal = decimal + rem * base;
base = base * 8;
temp = temp / 10;
}
temp = decimal;
while (temp > 0)
{
binary[i] = temp % 2;
temp = temp / 2;
i++;
}
printf("\nBinary number = ");
while (i > 0)
printf("%d", binary[--i]);
getch();
}
"""

        case "exp2":
            # Experiment 2: 1's and 2's Complement of a Number[cite: 34, 35]
            code = r"""#include<stdio.h>
#include<conio.h>
void main()
{
int a[20], ones [20], twos [20];
int n, i, carry = 1;
clrscr();
printf("Enter number of bits: ");
scanf("%d", &n);
printf("Enter binary number: ");
for ( i=0; i<n; i++)
scanf("%d", &a[i]);

for (i=0; i<n; i++)
/* 1's complement */
ones [i] = (a[i] == 0)?1:0;

for (i=n-1; i>=0; i--)
/* add 1 -> 2's complement */
{
if (carry == 1)
{
if (ones[i] == 1) {
twos[i] = 0; carry = 1; }
else
{
twos[i] = 1; carry = 0; }
}
else
twos [i] = ones[i];
}
printf("\n1's Complement = ");
for ( i=0; i<n; i++)
printf("%d", ones[i]);
printf("\n2's Complement = ");
for (i=0; i<n; i++)
printf("%d", twos[i]);
getch();
}"""

        case "exp3":
            # Experiment 3: Digital Circuits Using Logic Gates (Cedar Logic Simulator)[cite: 36, 37]
            code = r"""/* 
=========================================================
Experiment 3: Digital Circuits Using Logic Gates
=========================================================
Note: This is a hardware/software simulation experiment 
performed using the Cedar Logic Simulator. It involves 
placing and wiring Logic Gates (AND, OR, NOT, XOR) to 
build a Full Adder and Full Subtractor. 

There is no C or Assembly source code for this experiment.
=========================================================
*/"""

        case "exp4":
            # Experiment 4: Addition and Subtraction of Binary and Hexadecimal Numbers[cite: 38, 39, 40, 41]
            code = r"""
// ==========================================
// CODE 1: Binary Addition
// ==========================================
#include<stdio.h>
#include<conio.h>
void main()
{
int a, b, sum=0, carry = 0;
int digit, place = 1;
clrscr();
printf("Enter first binary number: ");
scanf("%d", &a);
printf("Enter second binary number: ");
scanf("%d", &b);
while (a>0 || b > 0)
{
digit = (a % 10) + (b % 10) + carry;
if (digit == 0)
{ sum = sum + 0 * place;
carry = 0; }
else if (digit == 1)
{ sum = sum + 1 * place;
carry = 0; }
else if (digit == 2)
{ sum = sum + 0 * place; carry = 1; }
else
{ sum = sum + 1 * place; carry = 1; }
a = a / 10;
b = b / 10;
place = place * 10;
}
if (carry == 1)
sum = sum + place;
printf("\nBinary Addition = %d", sum);
getch();
}

// ==========================================
// CODE 2: Binary Subtraction
// ==========================================
#include<stdio.h>
#include<conio.h>
void main()
{
int a, b, sub = 0, borrow = 0;
int digit, place = 1;
clrscr();
printf("Enter first binary number: ");
scanf("%d", &a);
printf("Enter second binary number: ");
scanf("%d", &b);
while (a > 0 || b > 0)
{
digit = (a % 10) - (b % 10) - borrow;
if (digit >= 0) { sub = sub + digit * place;
borrow = 0; }
else
{ sub = sub + (digit + 2) * place; borrow = 1; }
a = a / 10;
b = b / 10;
place = place * 10;
}
printf("\nBinary Subtraction = %d", sub);
getch();
}

// ==========================================
// CODE 3: Hexadecimal Addition
// ==========================================
#include <stdio.h>
#include <conio.h>
int hexToDec(char ch)
{
if (ch >= '0' && ch <= '9') return ch - '0';
else if (ch >= 'A' && ch <= 'F') return ch - 'A' + 10;
else return ch - 'a' + 10 ;
}
char decToHex(int n)
{
if (n < 10) return n + '0';
else return n - 10 + 'A' ;
}
void main()
{
char a[20], b[20], result [20];
int i, j, k, x, y, sum, carry = 0;
clrscr();
printf("Enter first hexadecimal number: ");
scanf("%s", a);
printf("Enter second hexadecimal number: ");
scanf("%s", b);
i = 0; while (a[i] != '\0') i++; i--; /* index of last digit */
j = 0; while (b[j] != '\0') j++; j--;
k = 0;
while (i >= 0 || j >= 0)
{
x = (i >= 0) ? hexToDec(a[i]) : 0;
y = (j >= 0) ? hexToDec(b[j]) : 0;
sum = x + y + carry;
if (sum >= 16) { result[k] = decToHex (sum - 16); carry = 1; }
else
{ result[k] = decToHex(sum);
carry = 0; }
k++; i--; j--;
}
if (carry == 1)
result[k++] = '1';
printf("Addition = ");
while (k > 0)
printf("%c", result[--k]);
getch();
}

// ==========================================
// CODE 4: Hexadecimal Subtraction
// ==========================================
#include <stdio.h>
#include <conio.h>
/* hexToDec() and decToHex() same as Code 3 */
void main()
{
char a[20], b[20], result[20];
int i, j, k, x, y, diff, borrow = 0;
clrscr();
printf("Enter first hexadecimal number: ");
scanf("%s", a);
printf("Enter second hexadecimal number: ");
scanf("%s", b);
i = 0; while (a[i] != '\0') i++; i--;
j = 0; while (b[j] != '\0') j++; j--;
k = 0;
while (i >= 0)
{
x = hexToDec(a[i]) - borrow;
y = (j >= 0) ? hexToDec(b[j]) : 0;
if (x < y) { x = x + 16; borrow = 1; }
else
{ borrow = 0; }
diff = x - y;
result [k] = decToHex(diff);
k++; i--; j--;
}
printf("Subtraction = ");
while (k > 0)
printf("%c", result[--k]);
getch();
}
"""

        case "exp5":
            # Experiment 5: Restoring Division Algorithm[cite: 43]
            code = r"""#include <stdio.h>
#include <conio.h>
typedef struct {
unsigned int quotient;
unsigned int remainder;
} DivResult;
DivResult restoringDivision (unsigned int dividend, unsigned int divisor)
{
unsigned int A = 0;
unsigned int Q = dividend;
unsigned int M = divisor;
int n = sizeof(unsigned int) * 8;
int i;
DivResult result;
for (i=0; i<n; i++)
{
A = (A << 1) | ((Q >> (n - 1)) & 1); /* shift AQ left */
Q = Q << 1;
A = A - M;
if ((A & (1u << (n - 1))) != 0)
{
A = A + M;
Q = Q & (~1u);
/* A negative -> restore */
/* Q0 = 0 */
}
else
Q = Q | 1;
/* Q0 = 1 */
}
result.quotient = Q;
result.remainder = A;
return result;
}
void main()
{
unsigned int dividend, divisor;
DivResult result;
printf("Enter dividend (unsigned): ");
scanf("%u", &dividend);
printf("Enter divisor (unsigned): ");
scanf("%u", &divisor);
result = restoringDivision (dividend, divisor);
printf("Quotient = %u\n", result.quotient);
printf("Remainder = %u\n", result.remainder);
getch();
}"""

        case "exp6":
            # Experiment 6: Non-Restoring Division Algorithm[cite: 45, 46]
            code = r"""#include <stdio.h>
#include <conio.h>
typedef struct {
unsigned int quotient;
unsigned int remainder;
} DivResult;
DivResult nonRestoringDivision (unsigned int dividend, unsigned int divisor)
{
unsigned int n = sizeof(unsigned int) * 8;
int i;
unsigned int Q = dividend;
unsigned int M = divisor;
int A = 0;
DivResult result;
for ( i=0; i<n; i++)
{
A = (A << 1) | ((Q & (1u << (n - 1))) ? 1 : 0); /* shift AQ left */
Q = Q << 1;
if (A < 0) A = A + M; /* previous A negative -> add */
else A = A - M;       /* previous A positive -> subtract */

if (A < 0) Q = Q & (~1u); /* Q0 = 0 */
else Q = Q | 1;           /* Q0 = 1 */
}
if (A < 0)
A = A + M; /* final correction */

result.quotient = Q;
result.remainder = (unsigned int)A;
return result;
}
void main()
{
unsigned int dividend, divisor;
DivResult result;
printf("Enter dividend (unsigned): ");
scanf("%u", &dividend);
printf("Enter divisor (unsigned): ");
scanf("%u", &divisor);
if (divisor == 0)
{
printf("Error: Division by zero is undefined.\n");
getch();
return;
}
result = nonRestoringDivision (dividend, divisor);
printf("Quotient = %u\n", result.quotient);
printf("Remainder = %u\n", result.remainder);
getch();
}"""

        case "exp7":
            # Experiment 7: 8086 ALP for Arithmetic Operations[cite: 48, 49, 50]
            code = r"""
; ==========================================
; CODE 1: Addition
; ==========================================
; Program to add two word-length numbers
OPR1: DW 0x0101 ; first number
OPR2: DW 0x0202 ; second number
RESULT: DW 0    ; place to store result
start:
MOV AX, word OPR1 ; first number ->AX
MOV BX, word OPR2 ; second number ->BX
CLC               ; clear carry flag
ADD AX, BX        ; AX=AX+BX
MOV CX, AX
MOV DI, OFFSET RESULT
MOV word [DI], AX ; store result
print reg         ; print registers

; ==========================================
; CODE 2: Subtraction
; ==========================================
; Program to subtract two word-length numbers
OPR1: DW 0x0202
OPR2: DW 0x0101
RESULT: DW 0
start:
MOV AX, word OPR1
MOV BX, word OPR2
CLC
SUB AX, BX        ; AX=AX-BX
MOV CX, AX
MOV DI, OFFSET RESULT
MOV word [DI], AX
print reg

; ==========================================
; CODE 3: Multiplication
; ==========================================
; Program to multiply two word-length numbers
OPR1: DW 0x0303
OPR2: DW 0x0202
RESULT: DW 0
start:
MOV AX, word OPR1
MOV BX, word OPR2
CLC
MUL BX            ; DX:AX = AX * BX
MOV CX, AX
MOV DI, OFFSET RESULT
MOV word [DI], AX ; store lower word
print reg

; ==========================================
; CODE 4: Division
; ==========================================
; Program to divide two word-length numbers
OPR1: DW 0x0004
OPR2: DW 0x0002
RESULT: DW 0
start:
MOV AX, word OPR1
MOV BX, word OPR2
CLC
DIV BX            ; AX=DX:AX/BX, DX=remainder
MOV CX, AX
MOV DI, OFFSET RESULT
MOV word [DI], AX ; store quotient
print reg
"""

        case "exp8":
            # Experiment 8: 8086 ALP to Find the Largest and Smallest Number[cite: 51, 52]
            code = r"""
; Program to find minimum and maximum of given values
vals:
DB 0x02
DB 0x03
DB 0x01
DB 0x04
DB 0x07
DB 0x08
DB 0x09
DB 0x0F
DB 0x0A
DB 0x0B
last:
DB 0     ; marks end of values (its offset = count)
MIN:
DB 0     ; minimum stored here
MAX:
DB 0     ; maximum stored here

start:
MOV SI, 0              ; SI -> first value
MOV CX, OFFSET last    ; CX = number of values
MOV AL, byte [SI]      ; AL = first value
back:
CMP byte [SI], AL      ; compare value with AL
JNC skip               ; value >= AL -> not smaller, skip
MOV AL, byte [SI]      ; new minimum
skip:
INC SI
LOOP back
MOV byte MIN, AL       ; store minimum

MOV SI, 0
MOV CX, OFFSET last
MOV AL, byte [SI]
back1:
CMP AL, byte [SI]      ; compare AL with value
JNC skipl              ; AL >= value -> skip
MOV AL, byte [SI]      ; new maximum
skipl:
INC SI
LOOP back1
MOV byte MAX, AL       ; store maximum
print mem: 15          ; print memory
"""

        case "exp9":
            # Experiment 9: Data Transfer Techniques[cite: 53, 54]
            code = r"""#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFFER_SIZE 100
char memory [BUFFER_SIZE]; // simulated memory buffer
char deviceData[] = "DATA_FROM_DEVICE"; // simulated I/O device data

// 1. Programmed I/O (Polling)
void programmed10() {
printf("\n[Programmed I/O Transfer Started...]\n");
for (int i=0; deviceData[i] != '\0'; i++) {
printf("Polling device... ");
memory[i] = deviceData[i];
printf("Transferred: %c\n", memory[i]);
}
memory [strlen(deviceData)] = '\0';
printf("Data transferred using Programmed I/O : %s\n", memory);
}

// 2. Interrupt-Driven I/O (simulated)
void interruptIO() {
printf("\n[Interrupt-Driven I/O Transfer Started...]\n");
printf("Waiting for interrupt...\n");
printf("Interrupt received. Transferring data...\n");
strcpy(memory, deviceData);
printf("Data transferred using Interrupt I/O : %s\n", memory);
}

// 3. DMA (simulated)
void dmaTransfer() {
printf("\n[DMA Transfer Started... CPU sets up DMA and continues working]\n");
printf("DMA Controller transferring data...\n");
strcpy(memory, deviceData);
printf("DMA Transfer Complete. CPU interrupted.\n");
printf("Data transferred using DMA: %s\n", memory);
}

int main() {
int choice;
do {
printf("\n--- Data Transfer Techniques ---\n");
printf("1. Programmed I/O \n");
printf("2. Interrupt-Driven I/O\n");
printf("3. DMA (Direct Memory Access)\n");
printf("4. Exit\n");
printf("Choose a method (1-4): ");
scanf("%d", &choice);
switch (choice) {
case 1: programmed10(); break;
case 2: interruptIO(); break;
case 3: dmaTransfer(); break;
case 4: printf("Exiting...\n"); break;
default: printf("Invalid choice. Try again.\n");
}
} while (choice != 4);
return 0;
}"""

        case "exp10":
            # Experiment 10: Concept of Instruction Pipelining[cite: 56, 57]
            code = r"""#include <stdio.h>
#include <string.h>
#define MAX_INSTRUCTIONS 5
char *stages[] = {"Fetch", "Decode", "Execute", "Memory", "Write-back"};

void simulate_pipeline(char instructions[] [20], int num) {
for (int cycle = 0; cycle < num + 4; cycle++) {
printf("\nClock Cycle %d:\n", cycle + 1);
for (int stage = 4; stage >= 0; stage--) {
int instr_index = cycle - stage;
if (instr_index >= 0 && instr_index < num) {
printf("Instruction %s in stage: %s\n",
instructions [instr_index], stages [stage]);
}
}
}
}

int main() {
char instructions [MAX_INSTRUCTIONS] [20] = {
"ADD R1, R2, R3",
"SUB R4, R5, R6",
"MUL R7, R8, R9",
"LOAD R1,100(R2)",
"STORE R3,200 (R4)"
};
simulate_pipeline (instructions, MAX_INSTRUCTIONS);
return 0;
}"""

        case _:
            code = "# Error: Experiment code not found. Available keys: exp1 through exp10."

    return Response(code, mimetype='text/plain')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
