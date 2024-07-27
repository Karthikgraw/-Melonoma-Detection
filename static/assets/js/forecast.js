let forecast_results=JSON.parse(document.getElementById("weather_forecast").textContent)
                  console.log(forecast_results)
          
                  // Loop through forecast days and create charts
                  const forecastday = forecast_results.forecast.forecastday.length;
                  for (let i = 0; i < forecastday; i++) {
                      // Extract hourly temperature data for each forecast day
                      const hourlyTemperatures = forecast_results.forecast.forecastday[i].hour.map(data => data.temp_c);
                      // Create a new canvas element for each chart
                      const canvas = document.createElement('canvas');
                      canvas.id = 'temperatureChart' + i; // Assign a unique ID for each canvas
                      document.querySelector('.card-body').appendChild(canvas);
          
                      // Get the canvas context
                      const ctx = canvas.getContext('2d');
          
                      // Create the chart
                      new Chart(ctx, {
                          type: 'line',
                          data: {
                              labels: forecast_results.forecast.forecastday[i].hour.map(data => data.time.substr(11, 5)), // Assuming hourly data
                              datasets: [{
                                  label: 'Hourly Temperature',
                                  data: hourlyTemperatures,
                                  backgroundColor: 'rgba(255, 99, 132, 0.2)', // Background color
                                  borderColor: 'rgba(255, 99, 132, 1)', // Border color
                                  borderWidth: 1
                              }]
                          },
                          options: {
                              plugins: {
                                  title: {
                                      display: true,
                                      text: forecast_results.forecast.forecastday[i].date // Set date as the title
                                  }
                              },
                              scales: {
                                  y: {
                                      beginAtZero: true
                                  }
                              }
                          }
                      });
                  }