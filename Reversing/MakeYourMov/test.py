
	enc_str : [0x014,0x088,0x058,0x144,0x090,0x09c,0x14c,0x0c8,0x0b8,0x084,0x0ba,0x070,0x0a6,0x024,0x064,0x04a,0x04e,0x05a,0x070,0x01a,0x010,0x056,0x01b,0x035,0x021,0x03e,0x009,0x03d,0x021,0x026]
	str : [0,0,0,0,0,0,0,0,0,0x0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] //redacted
	key :[0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74]

	Z: 0
	One: 1
	M : -1
	counter : 30
	c :30
	t :0 
	b : 2
	b1 :1
	b_t: 0
	sh_t: 0
	x : 10

	_main:  t,t,str(1);
	        str(1),str(1),str(3); 
	        str(3),str(3),str(7); 
	        str(7),str(7),t; 
	        t,t,str(2);
	        str(2),str(2),str(4); 
	        str(4),str(4),str(8); 
	        str(8),str(8),t; 
	        t,t,str(5);
	        str(5),str(5),str(6); 
	        str(6),str(6),t;      
	        t,t,str(9);
	        str(9),str(9),str(0); 
	        str(0),str(0),t;     

	        t,t,str(11);
	        str(11),str(11),str(13); 
	        str(13),str(13),str(17); 
	        str(17),str(17),t; 
	        t,t,str(12);
	        str(12),str(12),str(14); 
	        str(14),str(14),str(18); 
	        str(18),str(18),t; 
	        t,t,str(15);
	        str(15),str(15),str(16); 
	        str(16),str(16),t;      
	        t,t,str(19);
	        str(19),str(19),str(10); 
	        str(10),str(10),t;     

	        t,t,str(21);
	        str(21),str(21),str(23); 
	        str(23),str(23),str(27); 
	        str(27),str(27),t; 
	        t,t,str(22);
	        str(22),str(22),str(24); 
	        str(24),str(24),str(28); 
	        str(28),str(28),t;
	        t,t,str(25);
	        str(25),str(25),str(26);
	        str(26),str(26),t;  
	        t,t,str(29);
	        str(29),str(29),str(20);
	        str(20),str(20),t;
	        
	        func:   Z,str(0),key(0);        //str(n)=str(n)^key(n)
	                M,func(1),Z;            //*str(n)++
	                M,func(2),Z;            //*key(n)++
	                One,counter,Z;          //counter--
	                Z,counter,Z,f_end;      //counter==0 -> f_end
	                Z,Z,Z,func;             //loop to func
	        
	        f_end:counter,counter,11;       //counter=11
	        func2:  M,ch0(0),Z;             //*str++ for ch0
	                M,ch1(0),Z;             //*str++ for ch1
	                M,ls_loop(1),Z;         //*str(+9)++ for loop
	                One,counter,Z;          //counter--
	                Z,counter,Z,cont;       //counter=0->cont
	                b_t,b_t,b;              //b_t=b
	                sh_t,sh_t,Z;            //sh_t=0
	                t,t,Z;                  //t=0
	            ch0: str,t,Z;                   //t=-str(n)
	                Z,b_t,Z,func2;              //b_t==0 -> func2
	                ls_loop:t,str,Z;               //str(n)=-t
	                        t,t,Z;                 //t=0
	                    ch1:str,t,Z;               //t=-str(n)
	                        M,sh_t,Z;              //sh_t+=1
	                        sh_t,b_t,Z,func2;      //b_t<=sh_t->func2
	                        b_t,b_t,b,ls_loop;     // ls_loop

	        cont: counter,counter,11;       //counter=11
	        func3:  M,ch2(0),Z;             //*str++ ch2(n)
	                M,ch3(0),Z;             //*str++ ch3(n)
	                M,ls_loop2(1),Z;        //*str(+9)++ for loop2
	                One,counter,Z;          //counter--
	                Z,counter,Z,loop;       //counter=0->loop
	                b_t,b_t,b1;             //b_t=b1
	                sh_t,sh_t,Z;            //sh_t=0
	                t,t,Z;                  //t=0
	            ch2: str(9),t,Z;                //t=-str[9]
	                Z,b_t,Z,func3;              //b_t=0->func3
	                ls_loop2:t,str(9),Z;           //str(9)=-t
	                        t,t,Z;                 //t=0
	                    ch3:str(9),t,Z;            //t=-str[9]
	                        M,sh_t,Z;              //sh_t+1
	                        sh_t,b_t,Z,func3;      //b_t<=sh_t->func3
	                        b_t,b_t,b,ls_loop2;    //
	        loop: Z,Z,Z,loop;                   //END
	
