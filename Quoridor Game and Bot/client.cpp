#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h> 
#include <bits/stdc++.h>
#include "globals.h"


/* Complete the function below to print 1 integer which will be your next move 
   */
int N,M,K, total_time, player,opplayer,contin;
float TL;
float TL_old;
int om,oro,oc;
int m,r,c;

struct state pos;
bool*** walls;
int* osc_state;

int main(int argc, char *argv[]){
	srand (time(NULL));
	int sockfd = 0, n = 0;
	char recvBuff[1024];
	char sendBuff[1025];
	struct sockaddr_in serv_addr; 

	if(argc != 3){
		printf("\n Usage: %s <ip of server> <port no> \n",argv[0]);
		return 1;
	} 
	if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0){
		printf("\n Error : Could not create socket \n");
		return 1;
	} 
	memset(&serv_addr, '0', sizeof(serv_addr)); 
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(atoi(argv[2])); 

	if(inet_pton(AF_INET, argv[1], &serv_addr.sin_addr)<=0){
		printf("\n inet_pton error occured\n");
		return 1;
	} 
	if( connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0){
	   printf("\n Error : Connect Failed \n");
	   return 1;
	} 

	cout<<"Quoridor will start..."<<endl;
	memset(recvBuff, '0',sizeof(recvBuff));
	n = read(sockfd, recvBuff, sizeof(recvBuff)-1);
	recvBuff[n] = 0;
	sscanf(recvBuff, "%d %d %d %d %d", &player, &N, &M, &K, &total_time);
	int opplayer = (player)%2 + 1;
	cout<<"Player "<<player<<endl;
	cout<<"Time "<<total_time<<endl;
	cout<<"Board size "<<N<<"x"<<M<<" :"<<K<<endl;
	contin=3;
	char s[100];
	int x=1;
	TL = total_time;

	initAI();		//	1

	if(player == 1){
		memset(sendBuff, '0', sizeof(sendBuff)); 
		string temp;
	
	// AI 	2
	m =0 ; r = 2; c = M/2 + 1;
	pos.row = 2;
	pos.col = M/2 + 1;

		snprintf(sendBuff, sizeof(sendBuff), "%d %d %d", m, r , c);
		write(sockfd, sendBuff, strlen(sendBuff));
		memset(recvBuff, '0',sizeof(recvBuff));
		n = read(sockfd, recvBuff, sizeof(recvBuff)-1);
		recvBuff[n] = 0;
		sscanf(recvBuff, "%f %d", &TL, &contin);
		cout<<TL<<" "<<contin<<endl;
		if(contin==1){
			cout<<"You win!! Yayee!! :D ";
			x=0;
		}
		else if(contin==2){
			cout<<"Loser :P ";
			x=0;
		}
	}

	while(x){
		memset(recvBuff, '0',sizeof(recvBuff));
		n = read(sockfd, recvBuff, sizeof(recvBuff)-1);
		recvBuff[n] = 0;
		sscanf(recvBuff, "%d %d %d %d", &om,&oro,&oc,&contin);
		cout << "opmove: "<< om <<" "<<oro<<" "<<oc << " "<<contin<<endl;
		if(contin==1){
			cout<<"You win!! Yayee!! :D ";
			break;
		}
		else if(contin==2){
			cout<<"Loser :P ";
			break;
		}
		memset(sendBuff, '0', sizeof(sendBuff)); 
		string temp;
		
	// AI 	2
	set_op_mov();
	setmrc();
	cout << "move  : "<< m <<" "<< r <<" "<< c << " "<<contin<<endl;

		snprintf(sendBuff, sizeof(sendBuff), "%d %d %d", m, r , c);
		write(sockfd, sendBuff, strlen(sendBuff));
		memset(recvBuff, '0',sizeof(recvBuff));
			n = read(sockfd, recvBuff, sizeof(recvBuff)-1);
			recvBuff[n] = 0;
			sscanf(recvBuff, "%f %d", &TL, &contin);//d=3 indicates game continues.. d=2 indicates lost game, d=1 means game won.
		cout<<TL<<" "<<contin<<endl;
		if(contin==1){
			cout<<"You win!! Yayee!! :D ";
			break;
		}
		else if(contin==2){
			cout<<"Loser :P ";
			break;
		}

	}
	cout<<endl<<"The End"<<endl;
	return 0;
}
















