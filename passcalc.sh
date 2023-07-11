#!/usr/bin/zsh

echo "Alias: "
read alias
echo "Secret: "
read secret
echo "Lenght: "
read lenght

echo "${secret}${alias}" | sha512sum | base64 | fold -w ${lenght} | head -n 1
