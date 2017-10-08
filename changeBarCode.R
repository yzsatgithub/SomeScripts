#filename <- ""
#datadf <- read.table(filename, sep = "\t", header = T, row.names = 1, stringsAsFactors = F)
rdaFilename <- ""
load(rdaFilename)

rnames <- rownames(refinedGE)

for(i in 1:length(rnames)){
    basename <- strsplit(rnames[i], "\\.")[[1]]
    basename <- paste(basename[-length(basename)], collapse = ".")
    rownames(refinedGE)[i] <- basename
}

