def hospital_fee(**fee_dict):
	max_amount = 0
	# max_payer = []
	for payer, fee in fee_dict.items():
		if fee > max_amount:
			max_amount = fee
			max_payer = [payer]
		elif fee == max_amount:
			max_payer.append(payer)
	return max_amount, max_payer	

# hospital_fee(Neymar = 1000, Dembele = 600, Reus = 500, Bale = 1000)
max_amount, max_payer = hospital_fee(Neymar = 1000, Dembele = 600, Reus = 500, Bale = 1000)
print(f"Highest fee was {max_amount} tk which was paid by {', '.join(max_payer)}.")