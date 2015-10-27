#include "globals.h"

int max_depth = 4;
struct move answer;

void printstate(struct state& p){
	//cout << "m "<< p.row << " " << p.col << " " << p.num_walls  << "\n";
	//cout << "o " <<p.oprow << " "<< p.opcol << " " << p.opnum_walls << "\n";
}

void copystate(struct state& old, struct state& news){
	news.row = old.row;
	news.col = old.col;
	news.oprow = old.oprow;
	news.opcol = old.opcol;
	news.num_walls= old.num_walls;
	news.opnum_walls = old.opnum_walls;
}

void initAI(){
	pos.col = M/2 + 1;
	pos.opcol = M/2 + 1;
	pos.num_walls = K;
	pos.opnum_walls = K;
	TL_old = TL;

	if (player == 1){
		pos.row = 1;
		pos.oprow = N;
	}
	else {
		pos.row = N;
		pos.oprow = 1;
	}
	
	bfsdepth = new int[N*M];
	que = new int[N*M];
	walls = new bool**[N+1];
	
	for(int i =0 ; i < N+1 ; i++){
		walls[i] = new bool*[M+1];	
		for(int j=0; j < M+1; j++){
			walls[i][j] = new bool[2];
			walls[i][j][1] = 0;
			walls[i][j][2] = 0;
		}
	}

	for(int i =0 ; i < M + 1 ; i++){
		walls[0][i][0] = 1;
		walls[N][i][0] = 1;

	}
	for(int i =0 ; i < N + 1 ; i++){
		walls[i][0][1] = 1;
		walls[i][M][1] = 1;
	}

	osc_state = new int[(N+1)*(M+1)*K*K];
	for(int i = 0 ; i < (N+1)*(M+1)*K*K ; i++){
		osc_state[i] = 0;
	}
}

inline bool terminal(struct state& present ,int depth){
	return (depth == 1 || ( contin==3 && (	(player == 1 && (present.row == N || present.oprow ==1) ) 
										 || (player == 2 && (present.row == 1 || present.oprow ==N) ) ) ) );
}

void set_op_mov(){
	//cout << "opp" << endl;
	if(TL - TL_old >= 15 )
		max_depth -=1;
	if(max_depth < 3)
		max_depth = 3;
	if( TL < 2)
		max_depth = 2;
	TL_old = TL;
	cout << "dep " << max_depth << "\n"; 
	if (om == 0  ) {
		if (oro != 0 && oc != 0 ){
			pos.oprow = oro;
			pos.opcol = oc;					
		}
	}
	else{
		walls[oro -1][oc -1][om - 1 ] = 1;
		// validwalls[oro-1][oc-1][0] -= 1;
		// validwalls[oro-1][oc-1][1] -= 1;
		// if(om==1){
		// 	validwalls[oro-1][oc-2][0] -= 1;
		// 	validwalls[oro-1][oc][0] -= 1;
		// }
		// else{
		// 	validwalls[oro-2][oc-1][1] -= 1;
		// 	validwalls[oro][oc-1][1] -= 1;
		// }
		pos.opnum_walls -=1;
	}
}

inline void create(struct move& now, struct state& tempst){
	if(now.mov == 0){
		tempst.row = now.row;
		tempst.col = now.col;
	}
	else{
		tempst.num_walls -=1;
		walls[now.row ][now.col][now.mov -1] = 1;
	}
}

inline void undo(struct move& now){
	if( now.mov != 0){
		walls[now.row][now.col][now.mov -1] = 0;
	}
}

inline void create_opp(struct move& now, struct state& tempst){
	if(now.mov == 0){
		tempst.oprow = now.row;
		tempst.opcol = now.col;
	}
	else{
		tempst.opnum_walls -=1;
		walls[now.row][now.col][now.mov -1] = 1;
	}
}

int Minvalue(struct state& present, int depth, int alpha, int beta);

int Maxvalue(struct state& present ,int depth, int alpha, int beta){
	//cout << "Maxval "<< present.row <<  " "<< present.col << " "<< depth <<  "\n";

	vector<struct move > move_list = succesors(present,player);
	//cout << "succ end"<< endl;
	int max_child = numeric_limits<int>::min();
	for(int i =0 ; i < move_list.size(); i++){
		struct state tempst ;
		copystate(present,tempst);

		create(move_list[i],tempst);
		//cout <<"move ** m " << move_list[i].mov <<" "<< move_list[i].row <<" "<< move_list[i].col << "\n"; 
			// printstate(present);
			// cout << "eval "<< zcx << "\n";
		int child;
		if( terminal(tempst,depth) ){
			child = eval_board(tempst);
		}
		else {
			child = Minvalue( tempst,depth -1,alpha,beta );
		}
		undo(move_list[i]);
		// if(depth == max_depth && tempst.row == 4 && tempst.col == 7){
		// cout <<"move ** m " << move_list[i].mov <<" "<< move_list[i].row <<" "<< move_list[i].col << " " << child << "\t"; 
		// }
		if(depth == max_depth){
			if(move_list[i].mov == 0){
				if( ( (child - 1*osc_state[ ( (move_list[i].row *(M+1) + move_list[i].col)*K + pos.num_walls)*K + pos.opnum_walls ] )  > max_child)
				    && (child < 1000000) ) {
					//answer = move_list[i];
					max_child = child;
					cout << "google ***"<< child << " " << "\n";
					answer.row = move_list[i].row;
					answer.col = move_list[i].col;
					answer.mov = move_list[i].mov;
				}
			}
			else{
				if( ( child  > max_child) && (child < 1000000) ) {
					max_child = child;
					//answer = move_list[i];
					cout << "google ***"<< child << " " << "\n";
					answer.row = move_list[i].row;
					answer.col = move_list[i].col;
					answer.mov = move_list[i].mov;
				}	
			}

		}
		else if( (child > max_child) && (child < 1000000) ){
			max_child = child;
		}
		if (child > alpha && (child < 1000000) ) 	alpha = child;
		if (alpha >= beta)	return child;
	}
	return max_child;
}

int Minvalue(struct state& present ,int depth, int alpha, int beta){
	//cout << "Minval "<< present.row <<  " "<< present.col << " "<< depth <<  "\n";
			

	int min_child = numeric_limits<int>::max();
	vector<struct move > move_list = succesors(present,3-player);	
	//cout << "succend"<< endl;

	for(int i =0 ; i < move_list.size(); i++){
		struct state tempst;
		copystate(present,tempst);

		create_opp(move_list[i],tempst);
		//cout <<"move ** m " << move_list[i].mov <<" "<< move_list[i].row <<" "<< move_list[i].col << "\n"; 
		// printstate(present);
		// cout << "eval "<< zcx << "\n";
		int child;
		if( terminal(tempst, depth) ){
			child = eval_board(tempst);
		}
		else {
			child = Maxvalue( tempst,depth -1, alpha, beta );
		}
		// if(depth == max_depth - 1 && tempst.row == 4 && tempst.col == 7){
		// 	cout <<"opmove ** m " << move_list[i].mov <<" "<< move_list[i].row <<" "<< move_list[i].col << " " << child << "\t"; 
		// }
		
		undo(move_list[i]);
		if (child < min_child && child != numeric_limits<int>::min() ) min_child = child;
		if (child < beta && child != numeric_limits<int>::min() )	beta = child;
		if (alpha >= beta)	return child;
	}
	return min_child;
}

	
void Minimaxdecision(struct state& pres ,int depth){

	int value = Maxvalue(pres,depth,numeric_limits<int>::min(), numeric_limits<int>::max());
}

void setmrc(){
	//cout << "setmrc "<< pos.row << " "<< pos.col << "\n";
	//cout << "opp" << endl;
	Minimaxdecision(pos,max_depth);
	//cout << "---- **** ----" << "\n";
	m = answer.mov;
	if (answer.mov == 0){
		pos.row = answer.row;
		pos.col = answer.col;		
		r = answer.row;
		c = answer.col;
		//osc_state[answer.row][answer.col][pos.num_walls][pos.opnum_walls] += 1;
		osc_state[ ( (answer.row *(M+1) + answer.col)*K + pos.num_walls)*K + pos.opnum_walls ] += 1;		
	}
	else{
		walls[answer.row ][answer.col][answer.mov - 1 ] = 1;
		pos.num_walls -= 1;
		r = answer.row + 1;
		c = answer.col + 1;
	}
}