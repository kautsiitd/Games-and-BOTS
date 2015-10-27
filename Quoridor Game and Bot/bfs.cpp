#include "globals.h"

#define mp make_pair
using namespace std;
// global variables
//bool walls[N+1][M+1][2];					// walls are stored in zero index form [0] is horizontal walls and [1] is vertical walls
											// opponent last move om(type) oro(row) oc(column)
											// send answer in ans[3] (move,row,column)

// eval variables
int* que;
int* bfsdepth;
int eval(int playerno, int row,int col){
	if ((playerno == 1 && row == N ) || (playerno == 2 && row == 1 ))
		return 0;
	int head = 0 , tail = 0;
	for(int i = 0; i < N*M ; i++){
		bfsdepth[i] = -1;
	}
	que[tail++] = (row-1) *M + (col-1);
	bfsdepth[(row-1) *M + (col-1)] = 0;
	if(playerno==1){
		while( head != tail ){
			int cu_x = que[head]/M;
			int cu_y = que[head]%M;// zero based positions
			// down 
			if(cu_x+1<N && bfsdepth[(cu_x+1)*M + cu_y]== -1 && walls[cu_x+1][cu_y][0]==0 && walls[cu_x+1][cu_y+1][0]==0){
				if(playerno ==1 && cu_x+1==N-1){
					return bfsdepth[cu_x*M + cu_y] + 1;
				}
				bfsdepth[(cu_x+1)*M + cu_y]= bfsdepth[cu_x*M + cu_y] + 1;
				que[tail++] = (cu_x+1)*M + cu_y;
			}
			//right
			if(cu_y+1<M && bfsdepth[cu_x*M+cu_y+1]==-1 && walls[cu_x][cu_y+1][1]==0 && walls[cu_x+1][cu_y+1][1]==0){
				bfsdepth[(cu_x)*M + cu_y +1 ]= bfsdepth[cu_x*M + cu_y] + 1;
				que[tail++] = (cu_x)*M + cu_y + 1;
			}
			//left
			if(cu_y-1>=0 && bfsdepth[cu_x*M + cu_y-1]==-1 && walls[cu_x][cu_y][1]==0 && walls[cu_x+1][cu_y][1]==0){
				bfsdepth[(cu_x)*M + cu_y -1 ]= bfsdepth[cu_x*M + cu_y] + 1;
				que[tail++] = (cu_x)*M + cu_y - 1;
			}
			//top
			if(cu_x-1>=0 && bfsdepth[(cu_x-1)*M + cu_y]==-1 && walls[cu_x][cu_y][0]==0 && walls[cu_x][cu_y+1][0]==0){
				if(playerno ==2 && cu_x-1==0){
					return bfsdepth[cu_x*M + cu_y] + 1;
				}
				bfsdepth[(cu_x-1)*M + cu_y]= bfsdepth[cu_x*M + cu_y] + 1;
				que[tail++] = (cu_x-1)*M + cu_y;
			}
			head++;
		}
	}
	else{
		while( head != tail ){
			int cu_x = que[head]/M;
			int cu_y = que[head]%M;// zero based positions
			//top
			if(cu_x-1>=0 && bfsdepth[(cu_x-1)*M + cu_y]==-1 && walls[cu_x][cu_y][0]==0 && walls[cu_x][cu_y+1][0]==0){
				if(playerno ==2 && cu_x-1==0){
					return bfsdepth[cu_x*M + cu_y] + 1;
				}
				bfsdepth[(cu_x-1)*M + cu_y]= bfsdepth[cu_x*M + cu_y] + 1;
				que[tail++] = (cu_x-1)*M + cu_y;
			}
			//right
			if(cu_y+1<M && bfsdepth[cu_x*M+cu_y+1]==-1 && walls[cu_x][cu_y+1][1]==0 && walls[cu_x+1][cu_y+1][1]==0){
				bfsdepth[(cu_x)*M + cu_y +1 ]= bfsdepth[cu_x*M + cu_y] + 1;
				que[tail++] = (cu_x)*M + cu_y + 1;
			}
			//left
			if(cu_y-1>=0 && bfsdepth[cu_x*M + cu_y-1]==-1 && walls[cu_x][cu_y][1]==0 && walls[cu_x+1][cu_y][1]==0){
				bfsdepth[(cu_x)*M + cu_y -1 ]= bfsdepth[cu_x*M + cu_y] + 1;
				que[tail++] = (cu_x)*M + cu_y - 1;
			}
			// down 
			if(cu_x+1<N && bfsdepth[(cu_x+1)*M + cu_y]== -1 && walls[cu_x+1][cu_y][0]==0 && walls[cu_x+1][cu_y+1][0]==0){
				if(playerno ==1 && cu_x+1==N-1){
					return bfsdepth[cu_x*M + cu_y] + 1;
				}
				bfsdepth[(cu_x+1)*M + cu_y]= bfsdepth[cu_x*M + cu_y] + 1;
				que[tail++] = (cu_x+1)*M + cu_y;
			}
			head++;
		}
	}
	
	return numeric_limits<int>::max();
}


bool terminal(int depth){
	if(depth>4){
		return 1;
	}
	return 0;
}

