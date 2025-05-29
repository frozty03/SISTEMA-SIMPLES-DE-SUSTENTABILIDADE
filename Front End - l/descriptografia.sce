clc
clear
T = ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z']; 

A = [5 4;3 3];

TABELA = [1 3 5 7 9 11 15 17 19 21 23 25;1 9 21 15 3 19 7 23 11 5 17 25];

//INVERSA

det = (A(1,1)*A(2,2)-A(1,2)*A(2,1));
det = pmodulo(det,26);

ind=find(TABELA(1,:) == det)
inverso = TABELA(2,ind);

//Matriz Inversa

AI=inverso*[A(2,2) -A(1,2);-A(2,1) A(1,1)];

// vetor do texto codificado


CODIFICADO=[ "U"  "H"  "W"  "B"  "J"  "Q"  "J"  "A"  "A"  "I"  "M"  "V"  "F"  "Y"  "P"  "E"  "Y"  "B"  "V"  "K"];


[m n]=size(CODIFICADO);

for i=1:n
    I(:,i)=find(CODIFICADO(:,i)==T);
end

// SEPARAR EM DUPLAS DE LETRAS E MONTAR A MATRIZ DO TEXTO CODIFICADO

for i=1:(n/2)
    k=2*i-1;
    C(:,i)=[I(:,k);I(:,k+1)];
end

// Processo de decifragem

P=AI*C;

P=pmodulo(P,26);

[r s] = size(P)
for i=1:r
    for j=1:s
       if P(i,j)==0 then P(i,j)=26
       else P(i,j)=P(i,j)
      end 
   end     
end


// Exibindo o texto 
P=P';
for i=1:(n/2)
    k=2*i-1;
    TC(1,[k k+1])=P(i,:);
end


// indexação

S=T(1,TC)
printf('\n Mensagem decodificada')
disp(S)

