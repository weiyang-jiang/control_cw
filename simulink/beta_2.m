function beta = beta_2(decl, latitude, h, theta)
decl = deg2rad(decl);
latitude = deg2rad(latitude);
h = deg2rad(h);
theta = deg2rad(theta);
disp((sin(decl)*cos(latitude) - cos(h)*cos(decl)*sin(latitude))...
        /sin(theta))
beta = -acos((sin(decl)*cos(latitude) - cos(h)*cos(decl)*sin(latitude))...
        /sin(theta));
beta = rad2deg(beta);
end
