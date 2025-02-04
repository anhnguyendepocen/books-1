function [kk, rQ] = HeatTriElement(kx, ky, Q, coord)
% [kk, rQ] = HeatTriElement(kx, ky, Q, coord)
% Generates coefficient matrix of a triangular element for heat flow
% kx, ky = thermal conductivities in the x and y directions
% Q = Heat generation
% coord = coordinates at the element ends

x1=coord(1,1); y1=coord(1,2);
x2=coord(2,1); y2=coord(2,2);
x3=coord(3,1); y3=coord(3,2);
b1 = y2 - y3; b2 = y3 - y1; b3 = y1 - y2;
c1 = x3 - x2; c2 = x1 - x3; c3 = x2 - x1;
f1 = x2*y3 - x3*y2; f2 = x3*y1 - x1*y3; f3 = x1*y2 - x2*y1;
A = (f1 + f2 + f3)/2;
kxx = 1/(4*A)*kx*[b1^2, b1*b2, b1*b3;
    b1*b2, b2^2, b2*b3; b1*b3, b2*b3, b3^2];
kyy = 1/(4*A)*ky*[c1^2, c1*c2, c1*c3;
    c1*c2, c2^2, c2*c3; c1*c3, c2*c3, c3^2];
kk = kxx + kyy;
rQ = 1/3*Q*A*[1; 1; 1];
