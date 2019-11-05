#include <iostream>
#include <wasserstein.h>

int main(int argc, char** argv){
    
    std::vector<double> aw = {2,4,6,8,10,12,14,16,18,20};
    std::vector<double> av(10);
    std::iota(av.begin(), av.end(), 0);

    std::vector<double> bw = {1,2,3,4,5,6,7,8,9,10};
    std::vector<double> bv(10);
    std::iota(bv.begin(), bv.end(), 0);

    double dist = wasserstein(av,aw,bv,bw);
    std::cout << "The earth movers distance is: " << dist << std::endl;

    av = {0,3,0,0,0,1,0,0,0,0,0,1,0};
    aw = {2,4,6,8,10,12,14,16,18,20,22,24,26};
    bv = {0,2,1,0,0,1,0,0,1,0,5,0,0};
    bw = {2,4,6,8,10,12,14,16,18,20,22,24,26};

    dist = wasserstein(av,aw,bv,bw);
    std::cout << "The earth movers distance is: " << dist << std::endl;

    av = {3.4, 3.9, 7.5, 7.8};
    aw = {1.4, 0.9, 3.1, 7.2};
    bv = {4.5, 1.4};
    bw = {3.2, 3.5};

    dist = wasserstein(av,aw,bv,bw);
    std::cout << "The earth movers distance is: " << dist << std::endl;

    av = {0, 1};
    aw = {3, 1};
    bv = {0, 1};
    bw = {2, 2};

    dist = wasserstein(av,aw,bv,bw);
    std::cout << "The earth movers distance is: " << dist << std::endl;

    av = {0, 1, 3};
    aw = {1, 1, 1};
    bv = {5, 6, 8};
    bw = {1, 1, 1};

    dist = wasserstein(av,aw,bv,bw);
    std::cout << "The earth movers distance is: " << dist << std::endl;

}
