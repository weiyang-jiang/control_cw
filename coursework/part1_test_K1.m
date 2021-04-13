ceta = 3;
K2 = 0.05;
T = 20;
tao = 5;
IAT_state_list = [];
rising_time_list = [];
settle_time_list = [];
K1_list = [];
length_iter = 599;
for i = 1:length_iter
    K1 = i + (300-length_iter/2);
    K1_list(end + 1) = K1;
    SimOut = sim('part1_dynamic_model');
    IAT_state = IAT_part1_data(end, end);
    info = stepinfo(IAT_part1_data(:,end),IAT_part1_data(:,1),IAT_state);
    IAT_state_list(end + 1) = IAT_state;
    rising_time_list(end + 1) = info.RiseTime;
    settle_time_list(end + 1) = info.SettlingTime;
end

figure
plot(K1_list, rising_time_list);
% set(gca,"XTick",0:2:24);
% set(gca,"XTicklabel",["00:00","02:00","04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00","00:00"]);
% set(gca,"YTick",0:0.1:2.5);
title("Rising time change with K1","FontSize",20);
xlabel("K1","FontSize",20);
ylabel("Rising time (s)","FontSize",20);
% legend("Cooling plant sensible load: Zone 1","FontSize",20);

figure
plot(K1_list, settle_time_list);
% set(gca,"XTick",0:2:24);
% set(gca,"XTicklabel",["00:00","02:00","04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00","00:00"]);
% set(gca,"YTick",0:0.1:2.5);
title("Settling time change with K1","FontSize",20);
xlabel("K1","FontSize",20);
ylabel("Settling time (s)","FontSize",20);
% legend("Cooling plant sensible load: Zone 1","FontSize",20);

figure
plot(K1_list, IAT_state_list);
% set(gca,"XTick",0:2:24);
% set(gca,"XTicklabel",["00:00","02:00","04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00","00:00"]);
% set(gca,"YTick",0:0.1:2.5);
title("IAT state Temp change with K1","FontSize",20);
xlabel("K1","FontSize",20);
ylabel("IAT Temp (deg C)","FontSize",20);
% legend("Cooling plant sensible load: Zone 1","FontSize",20);

