readChannelID = 3594564;
readAPIKey = 'YOURE READ API KEY';

% Read data from ThingSpeak
data = thingSpeakRead(readChannelID, ...
    'Fields', 1, ...
    'NumPoints', 20, ...
    'ReadKey', readAPIKey);

% Calculate average and standard deviation
avgTemp = mean(data);
display(avgTemp, 'Average Temperature');

stdTemp = std(data);
display(stdTemp, 'Standard Deviation of Temperature');

% Read and plot the second field against time
[humidity, time] = thingSpeakRead(readChannelID, ...
    'Fields', 2, ...
    'NumPoints', 20, ...
    'ReadKey', readAPIKey);

plot(time, humidity, 'r', 'LineWidth', 2);
xlabel('Time');
ylabel('Humidity');
title('My Humidity Station at SSU');
grid on;
