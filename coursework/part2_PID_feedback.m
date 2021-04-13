Kp = 0.001;
Ki = 0.001;
Kd = 0;
N = 17.6036;

Kp_manual = 1.0764;
Ki_manual = 0.054815;
Kd_manual = 5.2328;

N_manual = 17.6036;

ceta = 3;
K2 = 0.05;
T = 20;
tao = 5;
K1 = 0.1;
cp = 1;
Thot_air = 35;
mass = 0.03;

IAT_state_list_part2 = [];
rising_time_list_part2 = [];
settle_time_list_part2 = [];
K1_list_part2 = [];
length_iter = 50;
for i = 1:length_iter
    SimOut_part2 = sim('part2_PID_feedback_control');
    IAT_state_part2 = part2_IAT_temp(end, end);
    info = stepinfo(part2_IAT_temp(:,end),part2_IAT_temp(:,1),IAT_state_part2);
    IAT_state_list_part2(end + 1) = IAT_state_part2;
    rising_time_list_part2(end + 1) = info.RiseTime;
    settle_time_list_part2(end + 1) = info.SettlingTime;
end