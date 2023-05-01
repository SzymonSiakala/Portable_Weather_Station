const headers = {
                    headers: {'Content-Type': 'application/json'}
                }
                
fetch("/api/Illuminance/2", {
                        method: "GET",
                        headers: headers
                        }).then(response => response.json())
                        .then(data => {
                                        const x = data['data'].map(function(d){ return d['time']})
                                        const y = data['data'].map(function(d){ return d['illuminance']})
                                        const chart_data = {
                                            labels: x,
                                            datasets: [{
                                            label: 'Illuminance',
                                            backgroundColor: 'rgb(102, 102, 0)',
                                            borderColor: 'rgb(204, 204, 0)',
                                            data: y,
                                            tension: 0.5
                                            }]
                                        };
                                        const config = {
                                            type: 'line',
                                            data: chart_data,
                                            options: {
                                                plugins: {
                                                    title: {
                                                        display: true,
                                                        text: 'Illuminance',
                                                        font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                        }
                                                    },
                                                    legend: {
                                                        display: false
                                                    }
                                                },
                                                scales: {
                                                    x: {
                                                        ticks: {
                                                            maxTicksLimit: 15,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    },
                                                    y: {
                                                        title: {
                                                          display: true,
                                                          text: 'lux',
                                                          font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                          }
                                                        },
                                                        ticks: {
                                                            maxTicksLimit: 10,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        };
                                        const linechart = new Chart(
                                            document.getElementById('illuminance_chart_7'),
                                            config
                                        );
                                        console.log(config)
                                    });

fetch("/api/UV_index/2", {
                        method: "GET",
                        headers: headers
                        }).then(response => response.json())
                        .then(data => {
                                        const x = data['data'].map(function(d){ return d['time']})
                                        const y = data['data'].map(function(d){ return d['uv_index']})
                                        const chart_data = {
                                            labels: x,
                                            datasets: [{
                                            label: 'UV index',
                                            backgroundColor: 'rgb(102, 51, 0)',
                                            borderColor: 'rgb(204, 102, 0)',
                                            data: y,
                                            tension: 0.5
                                            }]
                                        };
                                        const config = {
                                            type: 'line',
                                            data: chart_data,
                                            options: {
                                                plugins: {
                                                    title: {
                                                        display: true,
                                                        text: 'UV index',
                                                        font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                        }
                                                    },
                                                    legend: {
                                                        display: false
                                                    }
                                                },
                                                scales: {
                                                    x: {
                                                        ticks: {
                                                            maxTicksLimit: 15,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    },
                                                    y: {
                                                        title: {
                                                            display: true,
                                                            text: 'index',
                                                            font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                            }
                                                        },
                                                        ticks: {
                                                            maxTicksLimit: 10,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        };
                                        const linechart = new Chart(
                                            document.getElementById('uv_index_chart_7'),
                                            config
                                        );
                                        console.log(config)
                                    });

fetch("/api/Temperature/2", {
                        method: "GET",
                        headers: headers
                        }).then(response => response.json())
                        .then(data => {
                                        const x = data['data'].map(function(d){ return d['time']})
                                        const y = data['data'].map(function(d){ return d['temperature']})
                                        const chart_data = {
                                            labels: x,
                                            datasets: [{
                                            label: 'Temperature',
                                            backgroundColor: 'rgb(102, 0, 0)',
                                            borderColor: 'rgb(204, 0, 0)',
                                            data: y,
                                            tension: 0.5
                                            }]
                                        };
                                        const config = {
                                            type: 'line',
                                            data: chart_data,
                                            options: {
                                                plugins: {
                                                    title: {
                                                        display: true,
                                                        text: 'Temperature',
                                                        font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                        }
                                                    },
                                                    legend: {
                                                        display: false
                                                    }
                                                },
                                                scales: {
                                                    x: {
                                                        ticks: {
                                                            maxTicksLimit: 15,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    },
                                                    y: {
                                                        title: {
                                                            display: true,
                                                            text: '°C',
                                                            font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                            }
                                                        },
                                                        ticks: {
                                                            maxTicksLimit: 10,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        };
                                        const linechart = new Chart(
                                            document.getElementById('temperature_chart_7'),
                                            config
                                        );
                                        console.log(config)
                                    });

fetch("/api/Humidity/2", {
                        method: "GET",
                        headers: headers
                        }).then(response => response.json())
                        .then(data => {
                                        const x = data['data'].map(function(d){ return d['time']})
                                        const y = data['data'].map(function(d){ return d['humidity']})
                                        const chart_data = {
                                            labels: x,
                                            datasets: [{
                                            label: 'Humidity',
                                            backgroundColor: 'rgb(0, 0, 102)',
                                            borderColor: 'rgb(0, 0, 204)',
                                            data: y,
                                            tension: 0.5
                                            }]
                                        };
                                        const config = {
                                            type: 'line',
                                            data: chart_data,
                                            options: {
                                                plugins: {
                                                    title: {
                                                        display: true,
                                                        text: 'Humidity',
                                                        font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                        }
                                                    },
                                                    legend: {
                                                        display: false
                                                    }
                                                },
                                                scales: {
                                                    x: {
                                                        ticks: {
                                                            maxTicksLimit: 15,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    },
                                                    y: {
                                                        title: {
                                                            display: true,
                                                            text: '%',
                                                            font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                            }
                                                        },
                                                        ticks: {
                                                            maxTicksLimit: 10,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        };
                                        const linechart = new Chart(
                                            document.getElementById('humidity_chart_7'),
                                            config
                                        );
                                        console.log(config)
                                    });

fetch("/api/Air_pressure/2", {
                        method: "GET",
                        headers: headers
                        }).then(response => response.json())
                        .then(data => {
                                        const x = data['data'].map(function(d){ return d['time']})
                                        const y = data['data'].map(function(d){ return d['air_pressure']})
                                        const chart_data = {
                                            labels: x,
                                            datasets: [{
                                            label: 'Air pressure',
                                            backgroundColor: 'rgb(102, 0, 51)',
                                            borderColor: 'rgb(204, 0, 102)',
                                            data: y,
                                            tension: 0.5
                                            }]
                                        };
                                        const config = {
                                            type: 'line',
                                            data: chart_data,
                                            options: {
                                                plugins: {
                                                    title: {
                                                        display: true,
                                                        text: 'Air pressure',
                                                        font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                        }
                                                    },
                                                    legend: {
                                                        display: false
                                                    }
                                                },
                                                scales: {
                                                    x: {
                                                        ticks: {
                                                            maxTicksLimit: 15,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    },
                                                    y: {
                                                        title: {
                                                            display: true,
                                                            text: 'hPa',
                                                            font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                            }
                                                        },
                                                        ticks: {
                                                            maxTicksLimit: 10,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        };
                                        const linechart = new Chart(
                                            document.getElementById('air_pressure_chart_7'),
                                            config
                                        );
                                        console.log(config)
                                    });

fetch("/api/Altitude/2", {
                        method: "GET",
                        headers: headers
                        }).then(response => response.json())
                        .then(data => {
                                        const x = data['data'].map(function(d){ return d['time']})
                                        const y = data['data'].map(function(d){ return d['altitude']})
                                        const chart_data = {
                                            labels: x,
                                            datasets: [{
                                            label: 'Altitude',
                                            backgroundColor: 'rgb(0, 51, 102)',
                                            borderColor: 'rgb(102, 0, 204)',
                                            data: y,
                                            tension: 0.5
                                            }]
                                        };
                                        const config = {
                                            type: 'line',
                                            data: chart_data,
                                            options: {
                                                plugins: {
                                                    title: {
                                                        display: true,
                                                        text: 'Altitude',
                                                        font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                        }
                                                    },
                                                    legend: {
                                                        display: false
                                                    }
                                                },
                                                scales: {
                                                    x: {
                                                        ticks: {
                                                            maxTicksLimit: 15,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    },
                                                    y: {
                                                        title: {
                                                            display: true,
                                                            text: 'm',
                                                            font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                            }
                                                        },
                                                        ticks: {
                                                            maxTicksLimit: 10,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        };
                                        const linechart = new Chart(
                                            document.getElementById('altitude_chart_7'),
                                            config
                                        );
                                        console.log(config)
                                    });

fetch("/api/Compensated_voc/2", {
                        method: "GET",
                        headers: headers
                        }).then(response => response.json())
                        .then(data => {
                                        const x = data['data'].map(function(d){ return d['time']})
                                        const y = data['data'].map(function(d){ return d['compensated_voc']})
                                        const chart_data = {
                                            labels: x,
                                            datasets: [{
                                            label: 'Compensated VOC',
                                            backgroundColor: 'rgb(0, 102, 0)',
                                            borderColor: 'rgb(0, 204, 0)',
                                            data: y,
                                            tension: 0.5
                                            }]
                                        };
                                        const config = {
                                            type: 'line',
                                            data: chart_data,
                                            options: {
                                                plugins: {
                                                    title: {
                                                        display: true,
                                                        text: 'Compensated VOC',
                                                        font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                        }
                                                    },
                                                    legend: {
                                                        display: false
                                                    }
                                                },
                                                scales: {
                                                    x: {
                                                        ticks: {
                                                            maxTicksLimit: 15,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    },
                                                    y: {
                                                        title: {
                                                            display: true,
                                                            text: 'ppm',
                                                            font: {
                                                            size: 18,
                                                            style: 'normal',
                                                            family: 'Arial'
                                                            }
                                                        },
                                                        ticks: {
                                                            maxTicksLimit: 10,
                                                            font: {
                                                                size: 14,
                                                                style: 'normal',
                                                                family: 'Arial'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        };
                                        const linechart = new Chart(
                                            document.getElementById('compensated_voc_chart_7'),
                                            config
                                        );
                                        console.log(config)
                                    });