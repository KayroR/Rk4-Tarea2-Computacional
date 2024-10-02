Para este laboratorio se utiliza el metodo de para solución de ecuaciones diferenciales: Runge Kutta 4, en honor a Carl Runge y Martin Wilhelm Kutta. El metodo se basa en tomar la solución a un punto temporal y<sub>n+1</sub> con base en la solución en el punto temporal y<sub>n</sub> .Se tiene:

<center> k<sub>1</sub> := hf(t<sub>n</sub> , y<sub>n</sub> )
<center> k<sub>2</sub> := hf(t<sub>n</sub> + h/2, y<sub>n</sub> k<sub>1</sub> /2) 
<center> k<sub>3</sub> := hf(t<sub>n</sub> + h/2, y<sub>n</sub> + k<sub>2</sub> /2)
<center> k<sub>4</sub> := hf(t<sub>n</sub> + h, y<sub>n</sub> + k<sub>3</sub>)
<center> y<sub>n+1</sub> = y<sub>n</sub> = 1/6 (k<sub>1</sub> + 2k<sub>2</sub> +2k<sub>3</sub> + k<sub>4</sub>)


