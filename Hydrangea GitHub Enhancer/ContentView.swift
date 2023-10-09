//
//  ContentView.swift
//  Hydrangea GitHub Enhancer
//
//  Created by Acan on 2023/10/9.
//

import SwiftUI

struct ContentView: View {
    
    @State private var source: String = "https://api.github.com/users/zeyu-xie/repos?type=public"
    @State private var repos: Array<Repo> = []
    @State private var count: Int = 0
    
    var body: some View {
        VStack {
            ScrollView(showsIndicators: false) {
                VStack(alignment: .leading) {
                    Text("Hydrangea GitHub Enhancer")
                    Link(destination: URL(string: "https://zeyu-xie.github.io/Acan")!) {
                        Text("- Made by Acan")
                    }
                    Link(destination: URL(string: "https://github.com/zeyu-xie/Hydrangea-GitHub-Enhancer/tree/iOS")!) {
                        Text("- GitHub")
                    }
                    Divider()
                }.frame(alignment: .leading)
                VStack(alignment: .leading) {
                    ForEach(0..<count, id: \.self) { num in
                        
                        Text(String(repos[num].name!))
                        Divider()
                    }
                }.frame(alignment: .leading)
            }.padding()
        }
        .padding().onAppear {
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

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
