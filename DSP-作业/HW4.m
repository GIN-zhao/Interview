%ideal lowpass filter
flp_ideal = [ones(1,125),zeros(1,189)];

%% Kaiser design
delta = 0.18*pi;
A = -20*log10(0.0531);
beta = 0.5842*(A-21)^(0.4)+0.07886*(A-21);
M = (A-8)/(2.285*delta);
M = ceil(M);
alpha = M/2;
n = 0:M;
window = kaiser(M+1,beta);
h_kaiser = (sin(0.49*pi*(n-alpha))./(pi*(n-alpha)))'.*window;
h_kaiser((M/2)+1) = 0.49*window((M/2)+1);

figure(1)
%unit impulse response
subplot(3,2,1)
stem(n,h_kaiser,'b');
title('the unit impulse response')
grid on;
%magnitude response
subplot(3,2,3)
[h_kaiser_freq,w] = freqz(h_kaiser,1,314);
plot(w,20*log10(abs(h_kaiser_freq)),'b');
title('the magnitude response')
xlabel('w')
ylabel('|H(e^jw)|(dB)')
grid on;
%error function
subplot(3,2,5)
E_kaiser = flp_ideal' - abs(h_kaiser_freq);
% E_kaiser(126:182) = NaH;
plot(w(1:125),E_kaiser(1:125),'b');
hold on;
plot(w(183:314),E_kaiser(183:314),'b');
grid on;
title('the error function')

%% Parks-McClellan
F = [0.4,0.58];
A_P = [1,0];
DEV = [0.0531,0.085];
[N, Fo, Ao, W] = firpmord(F, A_P, DEV);
h_parks = firpm(N, Fo, Ao, W);
n_parks = 0:N;
%unit impulse response
subplot(3,2,2)
stem(n_parks,h_parks,'b');
title('the unit impulse response')
grid on;
%magnitude response
subplot(3,2,4)
[h_parks_freq,w] = freqz(h_parks,1,314);
plot(w,20*log10(abs(h_parks_freq)),'b');
title('the magnitude response')
xlabel('w')
ylabel('|H(e^jw)|(dB)')
grid on;
%error function
subplot(3,2,6)
E_parks = flp_ideal' - abs(h_parks_freq);
% E_kaiser(126:182) = NaH;
plot(w(1:125),E_parks(1:125),'b');
hold on;
plot(w(183:314),E_parks(183:314),'b');
grid on;
title('the error function')

%% the orders
M
N

