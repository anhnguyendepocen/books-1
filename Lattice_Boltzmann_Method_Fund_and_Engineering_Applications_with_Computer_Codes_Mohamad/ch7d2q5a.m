m=101;n=101;
w0=2./6.;
w=1./6.;
c2=1./3.;
dx=1.0;
dy=1.0;
u=0.1; v=0.4;
f0=zeros(m,n);f1=zeros(m,n);f2=zeros(m,n);f3=zeros(m,n);f4=zeros(m,n);
rho=zeros(m,n);x=zeros(m);y=zeros(n);fluxq=zeros(m);flux=zeros(m);
Tm=zeros(m);Z=zeros(n,m);
x(1)=0.0; y(1)=0.0;
for i=1:m-1
  x(i+1)=x(i)+dx;
end
for j=1:n-1
  y(j+1)=y(j)+dy;

end
alpha=1.0;
omega=1/(3.*alpha+0.5);
twall=1.0;
nstep=400;
for i=1:m

  f0(i,j)=w0*rho(i,j);
  f1(i,j)=w*rho(i,j);
  f2(i,j)=w*rho(i,j);
  f3(i,j)=w*rho(i,j);
  f4(i,j)=w*rho(i,j);

end
				%Collision:
for k1=1:nstep
  for j=1:n
    for i=1:m
      feq0=w0*rho(i,j);
      feq1=w*rho(i,j)*(1.+3.*u);
      feq2=w*rho(i,j)*(1.-3.*u);
      feq3=w*rho(i,j)*(1.+3.*v);
      feq4=w*rho(i,j)*(1.-3.*v);
      f0(i,j)=(1.-omega)*f0(i,j)+omega*feq0;
      f1(i,j)=(1.-omega)*f1(i,j)+omega*feq1;
      f2(i,j)=(1.-omega)*f2(i,j)+omega*feq2;
      f3(i,j)=(1.-omega)*f3(i,j)+omega*feq3;


      f4(i,j)=(1.-omega)*f4(i,j)+omega*feq4;

    end
  end

				% Streaming:
  for j=1:n
    for i=1:m-1
      f1(m-i+1,j)=f1(m-i,j);
      f2(i,j)=f2(i+1,j);
    end
  end
  for i=1:m
    for j=1:n-1
      f3(i,n-j+1)=f3(i,n-j);
      f4(i,j)=f4(i,j+1);
    end
  end
				%Boundary condition:

  for j=1:n
    f1(1,j)=twall-f2(1,j)-f0(1,j)-f3(1,j)-f4(1,j);
    f2(m,j)=f1(m,j);
  end
  for i=1:m
    f3(i,1)=f4(i,1);
    f4(i,n)=-f0(i,n)-f3(i,n)-f2(i,n)-f1(i,n);
  end

  for j=1:n    
    for i=1:m
      rho(i,j)=f1(i,j)+f2(i,j)+f0(i,j)+f3(i,j)+f4(i,j);
    end
  end

end
				%rotating matrix for contour plotting
for j=1:n
  for i=1:m
    Z(j,i)=rho(i,j);
  end
end

for i=1:n
  Tm(i)=rho(i,(n-1)/2);
end

figure(1)
plot(x,Tm,'LineWidth',2)

xlabel('X')
ylabel('T')

figure(2)
contour(Z,'showText','on','LineWidth',2)

