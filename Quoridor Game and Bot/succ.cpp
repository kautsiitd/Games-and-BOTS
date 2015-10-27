#include "globals.h"

inline void add_move(vector<struct move>& ans,int a , int b, int c){
	struct move temp;
	temp.mov = a;
	temp.row = b ;
	temp.col = c ;
	ans.push_back(temp);
}


void printmove(vector<struct move>& a){
	for(int i=0; i < a.size(); i++)
		printf("%d %d %d; ",a[i].mov,a[i].row,a[i].col);
	printf("\n");
}

int eval_board(struct state& present){
	//cout << "eval 1" << "\n";
	int a = 4*eval(player,present.row,present.col);
	//cout << player << " " << present.row << " " << present.col << "\n";
	//cout << "eval 2" << "\n";
	//cout << player << " " << present.row << " " << present.col << "\n";
	//cout << "eval 3" << "\n";
	int b = 4*eval(3-player,present.oprow,present.opcol);
	int c = 2*(present.num_walls - present.opnum_walls);
	if( a >= 10000000 || b >=1000000 ){
		return 10000000;
	}
	//cout << a << " "<< b << "\n";
	if( b == 0) 
		return (b-a+c-1000);
	if( a == 0)
		return (b-a+c+1000);
	// //cout << "pos: " << present.row << " " << present.col << " "<< present.num_walls << "; " ;
	// //cout << present.oprow << " " << present.opcol << " " << present.opnum_walls <<  ": ";
	// //cout << a << " " << b << " " << c << "\n";
	return b-a+c;	
}

inline int can_move_up(struct state& present, vector<struct move>& ans ){

	bool a = (walls[present.row -1][present.col -1 ][0] || walls[present.row -1][present.col][0]);
 	if (a) return 0;	// wall
	bool b = (present.opcol == present.col) && (present.oprow + 1 == present.row );
 	if (!b){
		add_move(ans,0,present.row-1,present.col); 		
 		return 1; // freeup
 	} 
 	bool c = (walls[present.oprow -1][present.opcol -1 ][0] || walls[present.oprow -1][present.opcol][0]);
 	if (!c){
 		add_move(ans,0,present.oprow -1,present.opcol);
	 	return 2;	// free jump	
 	} 
	bool d  = ( walls[present.oprow - 1][present.opcol][1] || walls[present.oprow][present.opcol][1] );
	bool e = (walls[present.oprow - 1][present.opcol -1 ][1] || walls[present.oprow][present.opcol -1][1] );
	if (!d && !e){
		add_move(ans,0,present.oprow,present.opcol - 1);
		add_move(ans,0,present.oprow,present.opcol + 1);
		return 3; // jump with wall ahead	
	} 
	if (!d ){
		add_move(ans,0,present.oprow,present.opcol + 1);
		return 4;		// jump with wall ahead, left	
	} 
	if (!e ){
		add_move(ans,0,present.oprow,present.opcol - 1);
		return 5;		// jump with wall ahead, right	
	} 
	return 6;
}

inline int can_move_down(struct state& present, vector<struct move>& ans ){
	bool a = (walls[present.row][present.col -1 ][0] || walls[present.row][present.col][0] );
	if (a) return 0;	// wall
	bool b = (present.opcol == present.col) && (present.oprow == present.row + 1);
 	if (!b){
 		add_move(ans,0,present.row+1,present.col); 		
 		return 1; // freedown	
 	} 
 	bool c = (walls[present.oprow][present.opcol -1 ][0] || walls[present.oprow][present.opcol][0]);
 	if (!c){
 		add_move(ans,0,present.oprow +1,present.opcol);
	 	return 2;	// free jump	
 	} 
 	bool d  = ( walls[present.oprow - 1][present.opcol][1] || walls[present.oprow][present.opcol][1] );
	bool e = (walls[present.oprow - 1][present.opcol -1 ][1] || walls[present.oprow][present.opcol -1][1] );
	if (!d && !e){
		add_move(ans,0,present.oprow,present.opcol - 1);
		add_move(ans,0,present.oprow,present.opcol + 1);
		return 3; // jump with wall down	
	} 
	if (!d ){
		add_move(ans,0,present.oprow,present.opcol + 1);
		return 4;		// jump with wall down left	
	} 
	if (!e ){
		add_move(ans,0,present.oprow,present.opcol - 1);
		return 5;		// jump with wall down right	
	}
	return 6;
}

inline int can_move_right(struct state& present, vector<struct move>& ans ){
	bool a  = ( walls[present.row - 1][present.col][1] || walls[present.row][present.col][1] );
	if (a) return 0;	// wall
	bool b = (present.opcol == present.col + 1 ) && (present.oprow == present.row );
 	if (!b){
 		add_move(ans,0,present.row,present.col+1); 		
 		return 1; // freeright	
 	} 
 	bool c = (walls[present.oprow -1 ][present.opcol ][1] || walls[present.oprow][present.opcol][1]);
 	if (!c){
 		add_move(ans,0,present.oprow ,present.opcol + 1);
	 	return 2;	// free jump	
 	}
 	bool d = (walls[present.oprow][present.opcol -1 ][0] || walls[present.oprow][present.opcol][0]);
 	bool e = (walls[present.oprow -1][present.opcol -1 ][0] || walls[present.oprow -1][present.opcol][0]);
	if (!d && !e){
		add_move(ans,0,present.oprow-1,present.opcol );
		add_move(ans,0,present.oprow+1,present.opcol );
		return 3; // jump with wall right	
	} 
	if (!d ){
		add_move(ans,0,present.oprow+1,present.opcol );
		return 4;		// jump with wall right up	
	} 
	if (!e ){
		add_move(ans,0,present.oprow-1,present.opcol );
		return 5;		// jump with wall right down	
	}
	return 6;				// no move right
}

inline int can_move_left(struct state& present, vector<struct move>& ans ){
	bool a = (walls[present.row - 1][present.col -1 ][1] || walls[present.row][present.col -1][1] );
	if (a) return 0;	// wall
	bool b = ( present.oprow == present.row ) && (present.opcol + 1== present.col  );
 	if (!b){
 		add_move(ans,0,present.row,present.col-1); 		
 		return 1; // freeleft	
 	}
 	bool c = (walls[present.oprow -1 ][present.opcol -1 ][1] || walls[present.oprow][present.opcol -1][1]);
 	if (!c){
 		add_move(ans,0,present.oprow ,present.opcol - 1);
	 	return 2;	// free jump	
 	}
 	bool d = (walls[present.oprow][present.opcol -1 ][0] || walls[present.oprow][present.opcol][0]);
 	bool e = (walls[present.oprow -1][present.opcol -1 ][0] || walls[present.oprow -1][present.opcol][0]);
	if (!d && !e){
		add_move(ans,0,present.oprow-1,present.opcol );
		add_move(ans,0,present.oprow+1,present.opcol );
		return 3; // jump with wall left
	} 
	if (!d ){
		add_move(ans,0,present.oprow+1,present.opcol );
		return 4;		// jump with wall left up	
	} 
	if (!e ){
		add_move(ans,0,present.oprow-1,present.opcol );
		return 5;		// jump with wall left down	
	}
	return 6;
}

inline int can_move_up_op(struct state& present, vector<struct move>& ans ){
	
	bool a = (walls[present.oprow -1][present.opcol -1 ][0] || walls[present.oprow -1][present.opcol][0]);
 	if (a) return 0;	// wall
	bool b = (present.col == present.opcol) && (present.row + 1 == present.oprow );
 	if (!b){
		add_move(ans,0,present.oprow-1,present.opcol); 		
 		return 1; // freeup
 	} 
 	bool c = (walls[present.row -1][present.col -1 ][0] || walls[present.row -1][present.col][0]);
 	if (!c){
 		add_move(ans,0,present.row -1,present.col);
	 	return 2;	// free jump	
 	} 
	bool d  = ( walls[present.row - 1][present.col][1] || walls[present.row][present.col][1] );
	bool e = (walls[present.row - 1][present.col -1 ][1] || walls[present.row][present.col -1][1] );
	if (!d && !e){
		add_move(ans,0,present.row,present.col - 1);
		add_move(ans,0,present.row,present.col + 1);
		return 3; // jump with wall ahead	
	} 
	if (!d ){
		add_move(ans,0,present.row,present.col + 1);
		return 4;		// jump with wall ahead, left	
	} 
	if (!e ){
		add_move(ans,0,present.row,present.col - 1);
		return 5;		// jump with wall ahead, right	
	} 
	return 6;
}

inline int can_move_down_op(struct state& present, vector<struct move>& ans ){
	bool a = (walls[present.oprow][present.opcol -1 ][0] || walls[present.oprow][present.opcol][0] );
	if (a) return 0;	// wall
	bool b = (present.col == present.opcol) && (present.row == present.oprow + 1);
 	if (!b){
 		add_move(ans,0,present.oprow+1,present.opcol); 		
 		return 1; // freedown	
 	} 
 	bool c = (walls[present.row][present.col -1 ][0] || walls[present.row][present.col][0]);
 	if (!c){
 		add_move(ans,0,present.row +1,present.col);
	 	return 2;	// free jump	
 	} 
 	bool d  = ( walls[present.row - 1][present.col][1] || walls[present.row][present.col][1] );
	bool e = (walls[present.row - 1][present.col -1 ][1] || walls[present.row][present.col -1][1] );
	if (!d && !e){
		add_move(ans,0,present.row,present.col - 1);
		add_move(ans,0,present.row,present.col + 1);
		return 3; // jump with wall down	
	} 
	if (!d ){
		add_move(ans,0,present.row,present.col + 1);
		return 4;		// jump with wall down left	
	} 
	if (!e ){
		add_move(ans,0,present.row,present.col - 1);
		return 5;		// jump with wall down right	
	}
	return 6;
}

inline int can_move_right_op(struct state& present, vector<struct move>& ans ){
	bool a  = ( walls[present.oprow - 1][present.opcol][1] || walls[present.oprow][present.opcol][1] );
	if (a) return 0;	// wall
	bool b = (present.col == present.opcol + 1 ) && (present.row == present.oprow );
 	if (!b){
 		add_move(ans,0,present.oprow,present.opcol+1); 		
 		return 1; // freeright	
 	} 
 	bool c = (walls[present.row -1 ][present.col ][1] || walls[present.row][present.col][1]);
 	if (!c){
 		add_move(ans,0,present.row ,present.col + 1);
	 	return 2;	// free jump	
 	}
 	bool d = (walls[present.row][present.col -1 ][0] || walls[present.row][present.col][0]);
 	bool e = (walls[present.row -1][present.col -1 ][0] || walls[present.row -1][present.col][0]);
	if (!d && !e){
		add_move(ans,0,present.row-1,present.col );
		add_move(ans,0,present.row+1,present.col );
		return 3; // jump with wall right	
	} 
	if (!d ){
		add_move(ans,0,present.row+1,present.col );
		return 4;		// jump with wall right up	
	} 
	if (!e ){
		add_move(ans,0,present.row-1,present.col );
		return 5;		// jump with wall right down	
	}
	return 6;				// no move right
}

inline int can_move_left_op(struct state& present, vector<struct move>& ans ){

	bool a = (walls[present.oprow - 1][present.opcol -1 ][1] || walls[present.oprow][present.opcol -1][1] );
	if (a) return 0;	// wall
	bool b = ( present.row == present.oprow ) && (present.col + 1== present.opcol  );
 	if (!b){
 		add_move(ans,0,present.oprow,present.opcol-1); 		
 		return 1; // freeleft	
 	}
 	bool c = (walls[present.row -1 ][present.col -1 ][1] || walls[present.row][present.col -1][1]);
 	if (!c){
 		add_move(ans,0,present.row ,present.col - 1);
	 	return 2;	// free jump	
 	}
 	bool d = (walls[present.row][present.col -1 ][0] || walls[present.row][present.col][0]);
 	bool e = (walls[present.row -1][present.col -1 ][0] || walls[present.row -1][present.col][0]);
	if (!d && !e){
		add_move(ans,0,present.row-1,present.col );
		add_move(ans,0,present.row+1,present.col );
		return 3; // jump with wall left
	} 
	if (!d ){
		add_move(ans,0,present.row+1,present.col );
		return 4;		// jump with wall left up	
	} 
	if (!e ){
		add_move(ans,0,present.row-1,present.col );
		return 5;		// jump with wall left down	
	}
	return 6;
}

void place_walls(struct state& present, vector <struct move>& ans){
	for(int i = 1; i < N  ; i++){
		for(int j=1 ; j < M ; j++ ){
			if (!( walls[i][j][0] || walls[i][j-1][0] || walls[i][j+1][0] || walls[i][j][1] )) {
				// if( present.num_walls + present.opnum_walls < 2*K ){
				// 	walls[i][j][0] = 1;
				// 	int a = eval(player,present.row,present.col);
				// 	////cout << "wall 7" << "\n";
				// 	int b = eval(3-player,present.oprow,present.opcol);
				// 	walls[i][j][0] = 0;
				// 	if (a != numeric_limits<int>::max() && b != numeric_limits<int>::max() ){
				// 		add_move(ans,1,i,j);	
				// 	}
				// }
				// else{
				// 	add_move(ans,1,i,j);
				// }
				add_move(ans,1,i,j);
			}
			if (!( walls[i][j][1] || walls[i-1][j][1] || walls[i+1][j][1] || walls[i][j][0] )){
				// if(present.num_walls + present.opnum_walls < 2*K){
				// 	walls[i][j][1] = 1;
				// 	int a = eval(player,present.row,present.col);
				// 	////cout << "wall 7" << "\n";
				// 	int b = eval(3-player,present.oprow,present.opcol);
				// 	walls[i][j][1] = 0;
				// 	if (a != numeric_limits<int>::max() && b != numeric_limits<int>::max() )
				// 		add_move(ans,2,i,j);
				// }
				// else{
				// 	add_move(ans,2,i,j);	
				// }				
				add_move(ans,2,i,j);
			}
		}
	}
}

vector < struct move > succesors(struct state& present, int playerno ){
	////cout << "succ" << "\n";
	vector<struct move > ans;
	if(playerno == player){
		if(contin == 3){
			////cout << "p1" << "\n";
			can_move_up(present,ans) ;
			////cout << "p2" << "\n";
			can_move_down(present,ans) ;
			////cout << "p3" << "\n";
			can_move_right(present,ans);
			////cout << "p4" << "\n";
			can_move_left(present,ans) ;	  	
			////cout << "p5" << "\n";
			if(present.num_walls > 0 ) place_walls(present,ans);
			////cout << "p6" << "\n";
		}
		else if ((player == 1 && contin ==32) || (player == 2 && contin == 31) ){
			if (!(walls[present.row -1][present.col -1 ][0] || walls[present.row -1][present.col][0]))
				add_move(ans,0,present.row-1,present.col);
			if (!(walls[present.row][present.col -1 ][0] || walls[present.row][present.col][0] ))
				add_move(ans,0,present.row+1,present.col);
			if (!( walls[present.row - 1][present.col][1] || walls[present.row][present.col][1] ))
				add_move(ans,0,present.row,present.col+1);
			if (!(walls[present.row - 1][present.col -1 ][1] || walls[present.row][present.col -1][1] ))
				add_move(ans,0,present.row,present.col-1);
			if(present.num_walls > 0 ) place_walls(present,ans);
		}
		else if((player == 1 && contin ==31) || (player == 2 && contin == 32) ){
			if(present.num_walls > 0 ){
				place_walls(present,ans);	
			} 
			add_move(ans,0,present.row,present.col);
		}
	}
	else{
		if (contin == 3 ) {
			////cout << "op1 " << "\n";
			can_move_up_op(present,ans) ;
			////cout << "op2" << "\n";
			can_move_down_op(present,ans) ;
			////cout << "op3" << "\n";
			can_move_right_op(present,ans);
			////cout << "op4" << "\n";
			can_move_left_op(present,ans) ;	  		
			////cout << "op5" << "\n";
			if(present.opnum_walls > 0 ) place_walls(present,ans);
			////cout << "op6" << "\n";
		}
		else if( ((player == 1 && contin == 31) || (player == 2 && contin == 32)) ){
			if (!(walls[present.oprow -1][present.opcol -1 ][0] || walls[present.oprow -1][present.opcol][0]))
				add_move(ans,0,present.oprow-1,present.opcol);
			if (!(walls[present.oprow][present.opcol -1 ][0] || walls[present.oprow][present.opcol][0] ))
				add_move(ans,0,present.oprow+1,present.opcol);
			if (!( walls[present.oprow - 1][present.opcol][1] || walls[present.oprow][present.opcol][1] ))
				add_move(ans,0,present.oprow,present.opcol+1);
			if (!(walls[present.oprow - 1][present.opcol -1 ][1] || walls[present.oprow][present.opcol -1][1] ))
				add_move(ans,0,present.oprow,present.opcol-1);
			if(present.opnum_walls > 0 ) place_walls(present,ans);
		}
		else if((player == 1 && contin ==32) || (player == 2 && contin == 31) ){
			if(present.opnum_walls > 0 ) {
				place_walls(present,ans);
			}
			add_move(ans,0,present.oprow,present.opcol);
		}
	}
	//printmove(ans);	
	return ans;
}
	