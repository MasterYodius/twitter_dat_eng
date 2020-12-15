pipeline{
	agent any
	stages{
		stage('Build'){
			steps{
				script{
					if(env.BRANCH_NAME != 'master'){
						echo 'Building docker image'
						
						bat 'docker build -t data-eng:latest ./src -f ./src/Dockerfile'
					}
				}	
			}
		}
		stage('Run' ){		
			steps{
				script{
					if(env.BRANCH_NAME != 'master'){
						echo ('Run the app')
						
						bat 'docker run --name PROJET -d -p 5000:5000 data-eng'
					}
				}	
				
			}
		}
		stage('Unit Test'){
			steps{
				script{
					if(env.BRANCH_NAME == 'features'){
						
						bat 'src/tests.exe'
						
					}
				}	
				
			}
		}
		
		stage('Release'){
			steps{
				script{
					if(env.BRANCH_NAME == 'develop'){
						
						bat 'git checkout -b release'
						
					}
				}	
				
			}
		}
		
		stage('Acceptance Test'){
			steps{
				script{
					if(env.BRANCH_NAME == 'release'){
						
						input 'Proceed with live deploy ?'
						
					}
				}	
				
			}
		}
		
		stage('Merge to Master branch'){
			steps{
				script{
					if(env.BRANCH_NAME == 'release'){
						
						
						

						bat 'git checkout -b master'
						
						bat 'git merge release'
						


						
					}
				}	
				
			}
		}
		
		
		stage('Stop Containers'){
			
			steps{
				script{
					if(env.BRANCH_NAME != 'master'){
						
						bat 'docker pause PROJET'
						bat 'docker container rm --force PROJET'
						bat 'docker image rm --force data-eng'
						
					}
				}	
				
			}
			
		}
	}
}
