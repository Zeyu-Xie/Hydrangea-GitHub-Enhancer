//
//  ContentView.swift
//  Hydrangea GitHub Enhancer
//
//  Created by Acan on 2023/10/9.
//

import SwiftUI

struct Repositories: View {
    
    @State private var source: String = "https://api.github.com/users/zeyu-xie/repos?type=public"
    @State private var repos: Array<Repo> = []
    @State private var count: Int = 0
    
    @State private var isAlert: Bool = false
    
    var body: some View {
        NavigationView {
            ScrollView(showsIndicators: false) {
                VStack(alignment: .leading) {
                    Link(destination: URL(string: "https://zeyu-xie.github.io/Acan")!) {
                        Image(systemName: "person")
                        Text("Made by Acan")
                    }.padding(.bottom).padding(.top)
                    Link(destination: URL(string: "https://github.com/zeyu-xie/Hydrangea-GitHub-Enhancer")!) {
                        Image(systemName: "house")
                        Text("GitHub")
                    }.padding(.bottom)
                    Divider()
                }.frame(alignment: .leading)
                VStack(alignment: .leading) {
                    ForEach(0..<count, id: \.self) { num in
                        
                        Link(destination: URL(string: repos[num].html_url!)!) {
                            Text(String(repos[num].name!)).foregroundColor(.black)
                        }
                        Text("")
                        
                        if(repos[num].homepage != nil) {
                            Link(destination: URL(string: repos[num].homepage!)!) {
                                Text("Homepage").foregroundColor(.gray)
                            }
                        }
                        
                        else {
                            Button("Homepage Unavaliable") {
                                isAlert = true
                            }.foregroundColor(.gray).alert(isPresented: $isAlert) {
                                Alert(title: Text("Homepage Not Existed"), message: Text("Inasmuch as this repository is publicly accessible, it regrettably lacks an associated homepage."), dismissButton: .default(Text("Back")))
                            }
                        }
                        
                        Divider()
                    }
                }.frame(alignment: .leading)
            }.padding(.leading).padding(.trailing).navigationTitle(Text("Repositories"))
        }.onAppear {
            getGitHubRepos()
        }
    }
    
    
    func getGitHubRepos() {
        if let url = URL(string: source) {
            let session = URLSession.shared
            let task = session.dataTask(with: url) { (data, response, error) in
                if let error = error {
                    print("ERROR：\(error)")
                } else if let data = data {
                    do {
                        repos = try JSONDecoder().decode(Array<Repo>.self, from: data)
                        count = repos.count
                    } catch {
                        print("ERROR：\(error)")
                    }
                    
                }
            }
            task.resume()
        }
    }
    
}
