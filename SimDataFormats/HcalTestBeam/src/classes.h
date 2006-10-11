#include "SimDataFormats/HcalTestBeam/interface/PHcalTB04Info.h"
#include "SimDataFormats/HcalTestBeam/interface/PHcalTB06Info.h"
#include "DataFormats/Common/interface/Wrapper.h"
#include <vector>

namespace {
  namespace {
    std::vector<int>                dumI;
    std::vector<float>              dumF;
    PHcalTB04Info                   theInfo4;
    edm::Wrapper<PHcalTB04Info>     theTB04Info;
    std::vector<PHcalTB06Info::Vtx> dummy1;
    std::vector<PHcalTB06Info::Hit> dummy2;
    PHcalTB06Info                   theInfo6;
    edm::Wrapper<PHcalTB06Info>     theTB06Info;
  }
}
