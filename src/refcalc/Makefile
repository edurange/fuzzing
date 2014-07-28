# Makefile

OBJS	= calc.tab.c

CC	= gcc

calc:		$(OBJS)
	$(CC) calc.tab.c -lm -o calc

calc.tab.c:
		bison -d calc.y

clean:		clobber
	rm calc

clobber:
	rm -f calc.tab.h calc.tab.c calc.output


