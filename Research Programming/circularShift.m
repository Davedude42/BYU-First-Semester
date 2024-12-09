

function M_shifted = circularShift(row)
    s_both = size(row);
    s = s_both(2);
    M_shifted = gf(zeros([s, s]));
    for row_of_M = 1:s
        for col_of_M = 1:s
            col_of_row = row_of_M - col_of_M + 1; % +1 because matlab is stupid and 1 indexed
            while col_of_row < 1
                col_of_row = col_of_row + s;
            end
            M_shifted(row_of_M, col_of_M) = row(1, col_of_row);
        end
    end
end