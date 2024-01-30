#/bin/bash/lua

function fact (n)
  if n == 0 then
    return 1
  else
    return n * fact(n-1)
  end
end

print("Hello!")
print("Enter a number to get its factorial:")
input = io.read("*nuamber")
print(string.format('%s! = %s', input, fact(input)))

