from mpmath import mpf, mp, mpc
from UnitTesting.standard_constants import precision

# Dictionary of trusted values to be used throughout files.
# Standard precision and seed values are precision: 30, seed: 1234.
# Note that changing these may drastically change the calculated values.

mp.dps = precision
trusted_values_dict = dict()

# Generated on: 2019-06-20 12:56:57.971661
trusted_values_dict['GiRaFFE_HOGlobals'] = {'uD[0]': mpf('0.356329850983273803398888342550422'), 'uD[1]': mpf('0.295581009991443068332165170363671'), 'uD[2]': mpf('0.571278676446695263693099384274148'), 'uU[0]': mpf('-0.183041405772196822712962219641404'), 'uU[1]': mpf('0.229039819108604088548750374634711'), 'uU[2]': mpf('0.0922166112633828069717823625990744'), 'gammaUU[0][0]': mpf('1.50832278893271522324443733509221'), 'gammaUU[0][1]': mpf('0.718941741855485791606640049320673'), 'gammaUU[0][2]': mpf('-1.3493207318971345328323750856787'), 'gammaUU[1][0]': mpf('0.718941741855485791606640049320673'), 'gammaUU[1][1]': mpf('-8.81229155581659057891998708661274'), 'gammaUU[1][2]': mpf('4.72002022524169987232643559122526'), 'gammaUU[2][0]': mpf('-1.3493207318971345328323750856787'), 'gammaUU[2][1]': mpf('4.72002022524169987232643559122526'), 'gammaUU[2][2]': mpf('-0.821267100447188242069288584146875'), 'gammadet': mpf('-0.065036041269854412884266892997947'), 'u0alpha': mpf('0.359941248753752646226258282224287'), 'alpsqrtgam': mpc(real='0.0', imag='0.176874818163846905417960140489501'), 'Stilde_rhsD[0]': mpc(real='0.499293091570658936462157638092236', imag='-3.77389815889249356228159979572496'), 'Stilde_rhsD[1]': mpc(real='0.859661259784586178252697277823387', imag='-3.74777930735730782417682400548999'), 'Stilde_rhsD[2]': mpc(real='2.25464740895651128526148271357276', imag='-4.21156661375156531276055075100216'), 'AevolParen': mpc(real='-0.784045915616820368945747543186054', imag='-2.27973412051449839839467116176479'), 'PevolParenU[0]': mpc(real='-0.597513485352304594293601897908085', imag='0.326034810293690255103940750232504'), 'PevolParenU[1]': mpc(real='-0.0637301776962939051647554370880003', imag='-0.837495910511803508983238537056802'), 'PevolParenU[2]': mpc(real='-0.317836706880516291708944730742059', imag='0.307043019604304583278413019407244'), 'A_rhsD[0]': mpc(real='-0.120908148968169726166816041681937', imag='0.0434897213915295514453681145478833'), 'A_rhsD[1]': mpc(real='-0.697675813401008145526738513220222', imag='0.0729086715271932708828703757893265'), 'A_rhsD[2]': mpc(real='-0.982294029767164830388592601151067', imag='-0.0947613350585148359512520195420886'), 'psi6Phi_rhs': mpf('-2.20082583378282623979774715485532')}
# Generated on: 2019-06-19 15:14:45.880872
trusted_values_dict['GiRaFFE_HO_v2Globals'] = {'gammaUU[0][0]': mpf('-12.4172704210817155780660711882973'), 'gammaUU[0][1]': mpf('12.4652931928177955657885238969456'), 'gammaUU[0][2]': mpf('2.05010202147649345811220787476174'), 'gammaUU[1][0]': mpf('12.4652931928177955657885238969456'), 'gammaUU[1][1]': mpf('-11.0799500210481356497847891453736'), 'gammaUU[1][2]': mpf('-2.34547540309616002232953533627102'), 'gammaUU[2][0]': mpf('2.05010202147649345811220787476174'), 'gammaUU[2][1]': mpf('-2.34547540309616002232953533627102'), 'gammaUU[2][2]': mpf('2.35651547094268947162822274210923'), 'gammadet': mpf('-0.0213006213368495431970918892118148'), 'SevolParenUD[0][0]': mpc(real='0.0', imag='-0.00408795521498870067360563739470187'), 'SevolParenUD[0][1]': mpc(real='0.0', imag='-0.0305369212661822483584362279196599'), 'SevolParenUD[0][2]': mpc(real='0.0', imag='-0.0907761643068746864027966833946702'), 'SevolParenUD[1][0]': mpc(real='0.0', imag='-0.0836105556143727944788047949935724'), 'SevolParenUD[1][1]': mpc(real='0.0', imag='0.0508140461488043757052053752728764'), 'SevolParenUD[1][2]': mpc(real='0.0', imag='-0.0893221437274709347853600408918172'), 'SevolParenUD[2][0]': mpc(real='0.0', imag='-0.0435816844597111680481059903261565'), 'SevolParenUD[2][1]': mpc(real='0.0', imag='-0.014963406412330404883233990553717'), 'SevolParenUD[2][2]': mpc(real='0.0', imag='0.0343221312064778102930963319616003'), 'Stilde_rhsD[0]': mpc(real='-0.588293264959852399780396765539662', imag='0.401905196272024176332281588053191'), 'Stilde_rhsD[1]': mpc(real='-0.789481776255265141762916423125064', imag='0.521971952889744213049675881088803'), 'Stilde_rhsD[2]': mpc(real='-0.784739252939226446972174260201629', imag='0.447710932145809255779679324935789'), 'AevolParen': mpc(real='-1.24341005013073586040269277460024', imag='-0.325683613772393264976746840639772'), 'PevolParenU[0]': mpc(real='-0.28918149430516308136149116526175', imag='-0.0662501271300850037259402496607303'), 'PevolParenU[1]': mpc(real='-0.268337985745965270362640698066059', imag='0.0828612605193133883531731177524996'), 'PevolParenU[2]': mpc(real='-0.304888534110494223958063101524057', imag='0.0116867205181466855533883409649675'), 'A_rhsD[0]': mpc(real='-0.954450607652970251254358778361204', imag='-0.0495410790649608008271814029642135'), 'A_rhsD[1]': mpc(real='-0.969158912337787880328707563437431', imag='0.000170231512009597657334498129522539'), 'A_rhsD[2]': mpc(real='-0.763038382428399942157724162730687', imag='0.0463159323463008545275193653286722'), 'psi6Phi_rhs': mpf('-1.5599310480531267767751072853914')}