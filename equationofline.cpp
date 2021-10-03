#include<stdio.h>
#include<conio.h>
#include<graphics.h>

int main()
{
int dx,dy,x1,x2,y1,y2,m,b,x,y,xnd;

int gdriver = DETECT, gmode, errorcode;

initgraph(&gdriver, &gmode, "");

printf("Enter x1,y1,x2,y2: ");
scanf("%d%d%d%d", &x1,&y1,&x2,&y2);

dx=x2-x1;
dy=y2-y1;
m=dy/dx;
b=y1-m*x1;

if(dx<0)
{
    x=x2;
    xnd=x1;
    y=y2;
}
if(dx>0)
{
    x=x1;
    xnd=x2;
    y=y1;
}
while(x<xnd)
{
    putpixel(x,y,WHITE);
    x=x+1;
    y=m*x+b;
}
getch();
}
