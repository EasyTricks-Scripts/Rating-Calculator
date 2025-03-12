

print("like oranı gir")
like = int(input())
print("dislike oranı gir")
dislike = int(input())


rating = like / (like + dislike)
rating_yuzde = rating*100

print("Beğenme oranı %", rating_yuzde)

##biraz internet
if ("rating_yuzde > 50"):
            print("İYİ")

elif("rating_yuzde == 50"):
             print("ORTA")

else:
    print("LEŞ GİBİ")






        

