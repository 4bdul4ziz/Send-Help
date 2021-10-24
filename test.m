clear all
clc
syms l1 l2 l3 t1 t2 x y z alph;

l1 = input('Enter link 1: ');
l2 = input('Enter link 2: ');
l3 = input('Enter link 3: ');

x = input('Enter x: ');
y = input('Enter y: ');
z = input('Enter z: ');

t1 = atand(y/x);

t2 = atand((z - l1)/(sqrt(x^2 + y^2)));

alph = round(sqrt(x^2 + y^2 + ((z - l1)^2)));

fprintf('\nThe theta1 in degrees is : %f',t1);
fprintf('\nThe theta2 in degrees is : %f',t2);
fprintf('\nThe alpha in degrees is : %f\n',alph);
