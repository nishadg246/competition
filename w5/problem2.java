import java.util.*;
import java.io.*;

public class problem2{
	public static void main(String[] args){
		String in1 = "";
		String rooms = "";
		String in3 = "";
		String in4 = "";
		try{
			BufferedREader br = new BufferedReader(new InputSreamReader(System.in));
			in1 = br.readLine();
			rooms = br.readLine();
			in3 = br.readLine();
			in4 = br.readLine();
		}catch(IOException e){
			e.printStackTrace();
		}

		int m = Integer.parseInt(in1.split(" ")[1])
		rooms.split(" ");
		for (int i)

	}
}
// data = sys.stdin.readlines()
// m=int(data[0].split(' ')[1])
// rooms=[int(a) for a in data[1].split(' ')]
// q=[int(a) for a in data[3].split(' ')]

// def calc(sums,a,m):
// 	tot=a*m
// 	i=0
// 	runtot=0
// 	q=sum(rooms)
// 	if q<=tot:
// 		return (len(rooms),(tot-q)%m)
// 	while i<len(rooms) and runtot+rooms[i]<=tot:
// 		runtot+=rooms[i]
// 		i+=1
// 	return (i,tot-runtot)


// h={}
// for a in q:
// 	if a in h:
// 		sys.stdout.write(str(h[a][0])+' '+str(h[a][1])+'\n')
// 	else:
// 		(z,y) = calc(rooms,a,m)
// 		sys.stdout.write(str(z)+' '+str(y)+'\n')
// 		h[a]=(z,y)
	