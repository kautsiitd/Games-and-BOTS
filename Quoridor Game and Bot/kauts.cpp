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
		// down 
		if(cu_x+1<N && bfsdepth[(cu_x+1)*M + cu_y]== -1 && walls[cu_x+1][cu_y][0]==0 && walls[cu_x+1][cu_y+1][0]==0){
			if(playerno ==1 && cu_x+1==N-1){
				return bfsdepth[cu_x*M + cu_y] + 1;
			}
			bfsdepth[(cu_x+1)*M + cu_y]= bfsdepth[cu_x*M + cu_y] + 1;
			que[tail++] = (cu_x+1)*M + cu_y;
		}
		//left
		if(cu_y-1>=0 && bfsdepth[cu_x*M + cu_y-1]==-1 && walls[cu_x][cu_y][1]==0 && walls[cu_x+1][cu_y][1]==0){
			bfsdepth[(cu_x)*M + cu_y -1 ]= bfsdepth[cu_x*M + cu_y] + 1;
			que[tail++] = (cu_x)*M + cu_y - 1;
		}
		head++;
	}
	return (20000000);
}


bool terminal(int depth){
	if(depth>4){
		return 1;
	}
	return 0;
}

/*
int eval(int playereval,int cu_x, int cu_y){		// one based positions		
	cout << playereval << cu_x << cu_y << endl;
	cout << "eval 3" << endl;
	cu_y = cu_y -1;
	cu_x = cu_x -1;								// zero based positions
	if ( (playereval == 2 && cu_x ==  0) || (playereval == 1 && cu_x == N-1))
		return 0;
	for(int i=0; i<N; i++){
		for (int j=0; j < M ; j++){
			bfsdepth[i][j] = 0;
		}
	}
	// bredth first search iterative
	cout << "eval 3" << endl;
	cout << "asdjfk" << endl;
	que< vector<int> > fringe;
	cout << "eval 3" << endl;
	
	int depth=0;
	vector<int> makep;
	makep.push_back(cu_x);makep.push_back(cu_y);makep.push_back(depth);
	fringe.push(makep);makep.clear();
		cout << "eval 4" << endl;

	while(!fringe.empty()){
		cu_x=fringe.front()[0];
		cu_y=fringe.front()[1];
		depth=fringe.front()[2];
		bfsdepth[cu_x][cu_y]=1;
		if(cu_x+1<N && bfsdepth[cu_x+1][cu_y]==0 && walls[cu_x+1][cu_y][0]==0 && walls[cu_x+1][cu_y+1][0]==0){
			if(playereval==1 && cu_x+1==N-1){
				return fringe.front()[2]+1;
			}
			makep.push_back(cu_x+1);makep.push_back(cu_y);makep.push_back(depth+1);
			fringe.push(makep);makep.clear();
			bfsdepth[cu_x+1][cu_y]=1;
		}
		if(cu_x-1>=0 && bfsdepth[cu_x-1][cu_y]==0 && walls[cu_x][cu_y][0]==0 && walls[cu_x][cu_y+1][0]==0){
			if(playereval==2 && cu_x-1==0){
				return fringe.front()[2]+1;
			}
			makep.push_back(cu_x-1);makep.push_back(cu_y);makep.push_back(depth+1);
			fringe.push(makep);makep.clear();
			bfsdepth[cu_x-1][cu_y]=1;
		}
		if(cu_y+1<M && bfsdepth[cu_x][cu_y+1]==0 && walls[cu_x][cu_y+1][1]==0 && walls[cu_x+1][cu_y+1][1]==0){
			makep.push_back(cu_x);makep.push_back(cu_y+1);makep.push_back(depth+1);
			fringe.push(makep);makep.clear();
			bfsdepth[cu_x][cu_y+1]=1;
		}
		if(cu_y-1>=0 && bfsdepth[cu_x][cu_y-1]==0 && walls[cu_x][cu_y][1]==0 && walls[cu_x+1][cu_y][1]==0){
			makep.push_back(cu_x);makep.push_back(cu_y-1);makep.push_back(depth+1);
			fringe.push(makep);makep.clear();
			bfsdepth[cu_x][cu_y-1]=1;
		}
		fringe.pop();
	}
	
	return numeric_limits<int>::max();
}
*/

