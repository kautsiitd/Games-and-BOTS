#ifndef _globals_h
#define _globals_h

#include <bits/stdc++.h>

using namespace std;

extern int N,M,K, total_time, player,contin;
extern float TL;
extern float TL_old;
extern int om,oro,oc;
extern int m,r,c;
extern int max_depth;
extern bool*** walls;
extern int* bfsdepth;
extern int* osc_state;

extern int* que;

struct state{
	int row,col,oprow,opcol;
	int num_walls, opnum_walls;
};

struct move{
	int mov;
	int row;
	int col;
};

extern struct state pos;

void setmrc();
void initAI();
void set_op_mov();
int eval(int player,int cu_x, int cu_y);
int eval_board(struct state& present);
vector < struct move > succesors(struct state& present, int player);

#endif
