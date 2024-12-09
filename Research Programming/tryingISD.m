

function [L_guess, c, message] = tryingISD(M0_transposed, dv, m)

s = size(M0_transposed);
p = s(1);

% Create M = [(M0')' | I]
M = gf(zeros(p, 2*p));
I = gf(eye(p));

M(1:p, 1:p) = M0_transposed';
M(1:p, p+1:2*p) = I;

% Max weight that the row we find can have
% Based on weight of first row of G and H
maxWeight = dv*2 * m;

n = 10000;

% Try n number of permutations

for i_ = 1:n
    % Generates a permutation of M (Mp) where 
    % the first chunk can be inverted
    while 1
    
        Mp = permuteRandomly(M);
        
        Mp_sub = Mp(1:p, 1:p);
        
        % Is invertible
        if rank(Mp_sub) == p
            break;
        end
    end
    
    
    % Guess is always [1, 0, ... 0]
    guess = zeros([1, p]);
    guess(1,1) = 1;
        
    
    % Find row and check weight
    
    % Used Mp_sub \ Mp instead of Mp instead of inv(Mp_sub) * Mp
    % because it's faster apparently
    row = guess * (Mp_sub \ M);
    
    % Find weight of row
    weight = 0;
    for j = 1:length(row)
        if row(1, j) == 1
           weight = weight + 1;
        end
    end
    
    % Verify row is low enough weight
    if weight < maxWeight
    
        % Also check if Lc' = 0
        
        % Create circular guess of L using our row
        % circular function didn't work for some reason
        L_guess = gf(zeros(p, 2*p));
        
        % The two chunks are circulated seperately
    
        L_guess(1:p, 1:p) = circularShift(row(1, 1:p));
        L_guess(1:p,  p+1:2*p) = circularShift(row(1, p+1:2*p));
        
        % Create Generator Matrix
        Gm = gf(zeros(p, 2*p));
        
        Gm(1:p, 1:p) = I;
        Gm(1:p, p+1:2*p) = M0_transposed;
        
        message = gf(zeros(1, p));

        % message should not be zero vector as that's an odd edge case
        while(1 && all(message == 0))
            % Random message to generate c with
            message = gf(randi([0, 1], 1, p));
        end
        
    
        c = message * Gm;
    
        % This vector being 0 means that L_guess is a valid key
        should_be_zero = L_guess * (c');
        
        % Checks if it is a zero vector
        if(1 && all(should_be_zero == 0)) 
            return;
        end
    end
end
    
     
disp("Attack failed.")
L_guess = [];
c = [];
message = [];