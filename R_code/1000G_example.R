#!/usr/bin/env RScript
#Simple code to parse a 1000G file
# and return a dict with mean allele
# frequency across populations




cal_mean_allele_frequency = function(row_dict){
	# Return a mean allele frequency from a dict with allele frequency values as input
	# Args:
		# row_dict: dict with population allele frequencies
	# Returns: 
		# float, mean allele frequency
	
	mean_af= mean(as.numeric(row_dict[c("EAS_AF",
																	 "AMR_AF",
																	 "AFR_AF",
																	 "EUR_AF")]))
	mean_af=round(mean_af, 3)
	return(mean_af)
}


read_csv = function(csv_file){
	data=read.csv(csv_file, 
							check.names=F,
							stringsAsFactors=F)	
	
	mean_allele_frequency=apply(data,1,function(x) cal_mean_allele_frequency(x))

	data$mean_allele_frequency= mean_allele_frequency			
							
	return(data)
}
