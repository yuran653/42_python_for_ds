ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[-1] = 'World!'

ft_tuple = ft_tuple[:-1] + ('Thailand!',)

ft_set.remove('tutu!')
ft_set.add('Bangkok!')

ft_dict['Hello'] = '42Bangkok!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
