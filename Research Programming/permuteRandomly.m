function MPermuted = permuteRandomly(M)
    s = size(M);
    n_cols = s(1);
    randomList = 1:n_cols;
    MPermuted = gf(zeros(size(M)));
    
    % Permutate M randomly
    for i = 1:n_cols
        
        randomIndex = randperm(length(randomList),1);
    
        MPermuted(:, randomList(randomIndex)) = M(:, i);
    
        randomList(randomIndex) = [];
    
    end
end