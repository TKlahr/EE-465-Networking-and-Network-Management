channelID = 3594616;

% Read CPU temperature and usage
[data, timestamps] = thingSpeakRead(channelID, ...
    'Fields', [1 2], ...
    'NumPoints', 60);

temperatureC = data(:, 1);
cpuPercent = data(:, 2);

% Convert CPU percentage to a fraction
cpuFraction = cpuPercent ./ 100;

% Calculate power
powerW = 2.3 * 100 .* cpuFraction + temperatureC .* 0.32;

% Plot power against time
plot(timestamps, powerW, 'b', 'LineWidth', 2);
xlabel('Time');
ylabel('Calculated Power (W)');
title('Raspberry Pi Power vs. Time');
grid on;
