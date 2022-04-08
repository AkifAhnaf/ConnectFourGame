#define COLUMNS 7
#define ROWS 6
#define MIN(A,B) ((A) < (B) ? (A) : (B))
double Chose[COLUMNS * ROWS + 1][COLUMNS * ROWS + 1];
main()
{
int Men;
double Total, Extra, Distributions();
Total = (double) 0;
InitChose();
for (Men = 0; Men <= COLUMNS * ROWS; Men++) {
Extra = Distributions(Men) * Chose[Men][Men/2];
printf("Total with %d men, is %.0f0, Men, Extra);
Total += Extra;
}
printf("Total number of positions on %d x %d board is at most %.0f0,
COLUMNS, ROWS, Total);
}
InitChose()
{
int i, j;
for (i = 0; i <= COLUMNS * ROWS; i++) {
Chose[i][0] = (double) 1;
for (j = 1; j < i; j++) {
Chose[i][j] = Chose[i-1][j] + Chose[i-1][j-1];
}
Chose[i][i] = (double) 1;
}
}
double
Distributions(Men)
int Men;
{
double Distribute();
return (Distribute(1, COLUMNS, (double) 1, Men));
double
Distribute(Row, UpperBound, Product, MenLeft)
int Row, UpperBound, MenLeft;
double Product;
{
int i;
double Sum;
if ((ROWS - Row + 1) * UpperBound < MenLeft) {
return ((double) 0);
}
if (Row > ROWS) {
return (Product);
}
Sum = (double) 0;
for (i = MIN(UpperBound, MenLeft); i >= 0; i--) {
Sum += Distribute(Row+1, i,
Product * Chose[UpperBound][i],
MenLeft - i);
}
return (Sum);
}
