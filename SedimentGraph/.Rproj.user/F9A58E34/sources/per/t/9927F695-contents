# this script takes the synthesized sediment data and then displays it as ca
# core log.

library(tidyr)
library(ggplot2)
library(dplyr)
library(RColorBrewer)
library(tcltk)
library(svglite)

sedGraph <- function(table, format=TRUE, greys=TRUE, savefile=FALSE){
  #Format the incoming table
  if(format != FALSE){
    table = table %>% group_by(DepthMeasured, SedClass) %>% #  Groups the table by sample depth and sediment class
            summarise(SedProp = (sum(ProportionOfSample, na.rm = TRUE))/100) #  applies sum to the sample proportion by the grouping
    table$SedClass = factor(table$SedClass, levels = list("Clay", "Silt", "Sand")) # converts SedClass into a factor and ranks grain size
    table$DepthMeasured = as.numeric(table$DepthMeasured) # Converts Depth Measured from binary/category into numeric
    table$DepthMeasure = sum(80 - table$DepthMeasured) # Inverts the depth measurment (samples were measured from the bottom of the core)
  }
  
  # Creating the plot
  plt = ggplot(table, aes(y=SedProp, 
                          x=DepthMeasured, 
                          group=SedClass, 
                          fill=SedClass)) +
                          geom_area() +  
                          coord_flip() + # Inverts the axes so that the graph is vertical
                          xlab('Depth of Sample (cm)') +      #{ \ 
                          ylab('Proportion of Grain Size') +  #{ - Labels x and y axes
                          scale_fill_brewer(palette = 'YlOrBr') +  #Default Colour
                          scale_x_continuous(expand = c(0, 0),
                                             breaks = seq(0,80,5)) +      #{ \
                          scale_y_continuous(expand = c(0, 0),            #{ - Sets 0,0 at the origin and relabels perecent axis (Y)
                                             labels = scales::percent) + 
                          theme(panel.border = element_rect(colour = "black", 
                                                            fill=NA, 
                                                            size=1.25)) + #places a border around the graph
                          
  
  #Conditionally formats to grescale depending on greys=TRUE argument
  if(greys == TRUE){
    plt= plt +scale_fill_brewer(palette = 'Greys')  #Greyscale
  }
  
  if(savefile != TRUE){
    return(plt)
  }
  else if(savefile == TRUE){
    folderpath = tk_choose.dir(default = '~', caption = 'Choose graph output folder')
    ggsave('SedimentGraphSVG.svg', path = folderpath )
    ggsave('SedimentGraphPNG.png', path = folderpath )
  }
}
  


