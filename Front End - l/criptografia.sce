clc
clear
T = ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z']; 
NOME = ['S' 'A' 'C' 'O' 'V' 'A' 'Z' 'I' 'O' 'N' 'A' 'O' 'P' 'A' 'R' 'A' 'E' 'M' 'P' 'E'];

[m n]=size(NOME)
for i=1:n
    I(:,i)=find(NOME(:,i)==T);
   
end

printf('\n Mensagem cifrada numérica')
disp(I)

for i=1:n/2;
    k=2*i-1;
    P(:,i)=[I(:,k) ;I(:,k+1)];
end
printf('\n Matriz da msg cifrada')
disp(P)


// Processo de criptografia

A = [5 4;3 3];

C=A*P;
C=pmodulo(C,26);


[li co]=size(C)

for i=1:li
    for j=1:co
    if C(i,j)==0 then C(i,j)=26
    else     C(i,j)=C(i,j);
end
end
end
printf('\n Matriz da msg codificada')
disp(C)

// exibindo o texto codificado

C=C';
for i=1:n/2;
    k=2*i-1
    TC(1,[k k+1])=C(i,:);
end

// INDEXAÇÃO
ME=T(1,TC)
printf('\n Mensagem codificada')
disp(ME)

